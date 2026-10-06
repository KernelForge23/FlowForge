import { supabase } from '../lib/supabase'

export type Workflow = {
  id: string
  user_id: string
  name: string
  enabled: boolean
}

export type Component = {
  type: string
  config: Record<string, unknown>
}

export type WorkflowDetail = Workflow & {
  trigger: Component
  conditions: Component[]
  actions: Component[]
}

export type Execution = {
  id: string
  workflow_id: string
  status: string
  trigger_data: Record<string, unknown>
  result: Record<string, unknown>
  error: string | null
}

const apiUrl = import.meta.env.VITE_API_URL ?? 'http://localhost:8000'

async function request<T>(path: string, options?: RequestInit): Promise<T> {
  const { data } = (await supabase?.auth.getSession()) ?? { data: { session: null } }
  const accessToken = data.session?.access_token
  const response = await fetch(`${apiUrl}${path}`, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...(accessToken ? { Authorization: `Bearer ${accessToken}` } : {}),
      ...(options?.headers ?? {}),
    },
  })
  if (!response.ok) {
    const body = await response.json().catch(() => ({}))
    throw new Error(typeof body.detail === 'string' ? body.detail : 'Request failed')
  }
  if (response.status === 204) return undefined as T
  return response.json() as Promise<T>
}

export const api = {
  listWorkflows: (userId: string) =>
    request<Workflow[]>(`/api/workflows?user_id=${encodeURIComponent(userId)}`),
  getWorkflow: (id: string) => request<WorkflowDetail>(`/api/workflows/${id}`),
  createWorkflow: (payload: unknown) =>
    request<Workflow>('/api/workflows', { method: 'POST', body: JSON.stringify(payload) }),
  updateWorkflow: (id: string, payload: unknown) =>
    request<WorkflowDetail>(`/api/workflows/${id}`, {
      method: 'PUT',
      body: JSON.stringify(payload),
    }),
  deleteWorkflow: (id: string) =>
    request<void>(`/api/workflows/${id}`, { method: 'DELETE' }),
  runWorkflow: (id: string, payload: Record<string, unknown>) =>
    request<Execution>(`/api/workflows/${id}/run`, {
      method: 'POST',
      body: JSON.stringify({ payload }),
    }),
  executions: (id: string) => request<Execution[]>(`/api/workflows/${id}/executions`),
}
