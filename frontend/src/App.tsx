import { useEffect, useState } from 'react'
import type { FormEvent } from 'react'
import type { Session } from '@supabase/supabase-js'
import { api } from './services/api'
import type { Component, Execution, GmailStatus, Workflow, WorkflowDetail } from './services/api'
import { supabase } from './lib/supabase'

const emptyComponent = (type: string): Component => ({ type, config: {} })

function App() {
  const [session, setSession] = useState<Session | null>(null)
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [workflows, setWorkflows] = useState<Workflow[]>([])
  const [selected, setSelected] = useState<WorkflowDetail | null>(null)
  const [executions, setExecutions] = useState<Execution[]>([])
  const [name, setName] = useState('')
  const [triggerType, setTriggerType] = useState('manual')
  const [condition, setCondition] = useState<Component | null>(null)
  const [conditionField, setConditionField] = useState('')
  const [conditionValue, setConditionValue] = useState('')
  const [actionType, setActionType] = useState('noop')
  const [actionConfig, setActionConfig] = useState('{}')
  const [emailTo, setEmailTo] = useState('')
  const [emailSubject, setEmailSubject] = useState('')
  const [emailText, setEmailText] = useState('')
  const [emailHtml, setEmailHtml] = useState('')
  const [enabled, setEnabled] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [busy, setBusy] = useState(false)
  const [gmail, setGmail] = useState<GmailStatus>({ connected: false, email: null })

  useEffect(() => {
    if (!supabase) return
    void supabase.auth.getSession().then(({ data }) => setSession(data.session))
    const { data } = supabase.auth.onAuthStateChange((_event, nextSession) => setSession(nextSession))
    return () => data.subscription.unsubscribe()
  }, [])

  useEffect(() => {
    const query = new URLSearchParams(window.location.search)
    const gmailResult = query.get('gmail')
    const detail = query.get('detail')
    if (gmailResult === 'error') {
      setError(detail ?? `Gmail connection failed (${query.get('reason') ?? 'unknown error'})`)
      window.history.replaceState({}, '', window.location.pathname)
    }
  }, [])

  useEffect(() => {
    if (session?.user.id) void refreshWorkflows(session.user.id)
  }, [session?.user.id])

  useEffect(() => {
    if (session?.user.id) {
      void api.gmailStatus().then(setGmail).catch(() => setGmail({ connected: false, email: null }))
    }
  }, [session?.user.id])

  async function refreshWorkflows(userId: string) {
    try {
      setWorkflows(await api.listWorkflows(userId))
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : 'Could not load workflows')
    }
  }

  async function login(event: FormEvent) {
    event.preventDefault()
    if (!supabase) {
      setError('Configure VITE_SUPABASE_URL and VITE_SUPABASE_ANON_KEY first.')
      return
    }
    setBusy(true)
    setError(null)
    const { error: loginError } = await supabase.auth.signInWithPassword({ email, password })
    setBusy(false)
    if (loginError) setError(loginError.message)
  }

  function loadBuilder(workflow: WorkflowDetail | null) {
    setSelected(workflow)
    setName(workflow?.name ?? '')
    setEnabled(workflow?.enabled ?? true)
    setTriggerType(workflow?.trigger.type ?? 'manual')
    const firstCondition = workflow?.conditions[0] ?? null
    setCondition(firstCondition)
    setConditionField(typeof firstCondition?.config.field === 'string' ? firstCondition.config.field : '')
    setConditionValue(typeof firstCondition?.config.value === 'string' ? firstCondition.config.value : '')
    const action = workflow?.actions[0] ?? emptyComponent('noop')
    setActionType(action.type)
    setActionConfig(JSON.stringify(action.config, null, 2))
    setEmailTo(Array.isArray(action.config.to) ? action.config.to.filter((item): item is string => typeof item === 'string').join(', ') : '')
    setEmailSubject(typeof action.config.subject === 'string' ? action.config.subject : '')
    setEmailText(typeof action.config.text === 'string' ? action.config.text : '')
    setEmailHtml(typeof action.config.html === 'string' ? action.config.html : '')
  }

  async function selectWorkflow(workflow: Workflow) {
    setError(null)
    try {
      const detail = await api.getWorkflow(workflow.id)
      loadBuilder(detail)
      setExecutions(await api.executions(workflow.id))
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : 'Could not load workflow')
    }
  }

  async function saveWorkflow(event: FormEvent) {
    event.preventDefault()
    if (!session?.user.id || !name.trim()) return
    let parsedAction: Record<string, unknown> = {}
    if (actionType === 'email') {
      const recipients = emailTo.split(',').map((item) => item.trim()).filter(Boolean)
      if (recipients.length === 0 || !emailSubject.trim() || (!emailText.trim() && !emailHtml.trim())) {
        setError('Email requires recipients, a subject, and text or HTML content')
        return
      }
      parsedAction = {
        to: recipients,
        subject: emailSubject.trim(),
        ...(emailText ? { text: emailText } : {}),
        ...(emailHtml ? { html: emailHtml } : {}),
      }
    } else {
      try {
        const value: unknown = JSON.parse(actionConfig)
        if (typeof value !== 'object' || value === null || Array.isArray(value)) throw new Error('Action config must be a JSON object')
        parsedAction = value as Record<string, unknown>
      } catch (caught) {
        setError(caught instanceof Error ? caught.message : 'Invalid action JSON')
        return
      }
    }
    const conditions = condition
      ? [{ type: condition.type, config: { field: conditionField, value: conditionValue } }]
      : []
    const payload = {
      name,
      enabled,
      trigger: { type: triggerType, config: triggerType === 'webhook' ? { source: 'github' } : {} },
      conditions,
      actions: [{ type: actionType, config: parsedAction }],
    }
    setBusy(true)
    setError(null)
    try {
      if (selected) {
        await api.updateWorkflow(selected.id, payload)
      } else {
        await api.createWorkflow({ user_id: session.user.id, ...payload })
      }
      await refreshWorkflows(session.user.id)
      setName('')
      loadBuilder(null)
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : 'Could not save workflow')
    } finally {
      setBusy(false)
    }
  }

  async function deleteWorkflow() {
    if (!selected || !window.confirm(`Delete "${selected.name}"?`)) return
    setBusy(true)
    try {
      await api.deleteWorkflow(selected.id)
      if (session?.user.id) await refreshWorkflows(session.user.id)
      loadBuilder(null)
      setExecutions([])
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : 'Could not delete workflow')
    } finally {
      setBusy(false)
    }
  }

  async function runWorkflow() {
    if (!selected) return
    setBusy(true)
    setError(null)
    try {
      await api.runWorkflow(selected.id, { source: 'dashboard' })
      setExecutions(await api.executions(selected.id))
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : 'Could not run workflow')
    } finally {
      setBusy(false)
    }
  }

  async function disconnectGmail() {
    setBusy(true)
    try {
      await api.disconnectGmail()
      setGmail({ connected: false, email: null })
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : 'Could not disconnect Gmail')
    } finally {
      setBusy(false)
    }
  }

  async function connectGmail() {
    setBusy(true)
    setError(null)
    try {
      const response = await api.connectGmail()
      window.location.href = response.authorization_url
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : 'Could not start Gmail connection')
      setBusy(false)
    }
  }

  if (!session) {
    return (
      <main className="auth-shell">
        <section className="card auth-card">
          <p className="eyebrow">FLOWFORGE</p>
          <h1>Automate the work between your tools.</h1>
          <p className="muted">Sign in to configure triggers, conditions, and actions.</p>
          <form onSubmit={login}>
            <label>Email<input type="email" value={email} onChange={(event) => setEmail(event.target.value)} required /></label>
            <label>Password<input type="password" value={password} onChange={(event) => setPassword(event.target.value)} required /></label>
            <button disabled={busy}>{busy ? 'Signing in…' : 'Sign in'}</button>
          </form>
          {error && <p className="error">{error}</p>}
        </section>
      </main>
    )
  }

  return (
    <main className="app-shell">
      <header className="topbar">
        <div><p className="eyebrow">FLOWFORGE</p><p className="muted">Workflow operations</p></div>
        <button className="secondary" onClick={() => void supabase?.auth.signOut()}>Sign out</button>
      </header>
      <section className="content">
        <div className="page-heading"><p className="eyebrow">WORKFLOWS</p><h1>Your automations</h1></div>
        <section className="card">
          <div className="detail-heading">
            <div><h2>Gmail connection</h2><p className="muted">{gmail.connected ? `Connected as ${gmail.email}` : 'Connect Gmail to send email actions from your account.'}</p></div>
            {gmail.connected ? <button className="secondary" onClick={() => void disconnectGmail()} disabled={busy}>Disconnect</button> : <button onClick={() => void connectGmail()} disabled={busy}>Connect Gmail</button>}
          </div>
        </section>
        <div className="grid">
          <section className="card">
            <h2>{selected ? 'Edit workflow' : 'Create workflow'}</h2>
            <form onSubmit={saveWorkflow}>
              <label>Name<input value={name} onChange={(event) => setName(event.target.value)} required /></label>
              <label>Trigger<select value={triggerType} onChange={(event) => setTriggerType(event.target.value)}><option value="manual">Manual</option><option value="webhook">GitHub webhook</option></select></label>
              <label className="checkbox"><input type="checkbox" checked={enabled} onChange={(event) => setEnabled(event.target.checked)} /> Enabled</label>
              <label>Condition<select value={condition?.type ?? ''} onChange={(event) => setCondition(event.target.value ? emptyComponent(event.target.value) : null)}><option value="">No condition</option><option value="equals">Equals</option><option value="contains">Contains</option><option value="not_equals">Not equals</option></select></label>
              {condition && <div className="two-col"><input placeholder="Payload field" value={conditionField} onChange={(event) => setConditionField(event.target.value)} /><input placeholder="Expected value" value={conditionValue} onChange={(event) => setConditionValue(event.target.value)} /></div>}
              <label>Action<select value={actionType} onChange={(event) => setActionType(event.target.value)}><option value="noop">No-op</option><option value="http">HTTP request</option><option value="github">GitHub dispatch</option><option value="email">Email</option></select></label>
              {actionType === 'email' ? <><p className="muted">{gmail.connected ? `Sends from ${gmail.email}` : 'Connect Gmail before running this action.'}</p><label>Recipients (comma-separated)<input type="text" placeholder="you@example.com" value={emailTo} onChange={(event) => setEmailTo(event.target.value)} /></label><label>Subject<input type="text" value={emailSubject} onChange={(event) => setEmailSubject(event.target.value)} /></label><label>Text body<textarea rows={4} value={emailText} onChange={(event) => setEmailText(event.target.value)} /></label><label>HTML body (optional)<textarea rows={4} value={emailHtml} onChange={(event) => setEmailHtml(event.target.value)} /></label></> : actionType !== 'noop' && <label>Action configuration (JSON)<textarea rows={5} value={actionConfig} onChange={(event) => setActionConfig(event.target.value)} /></label>}
              <div className="button-row"><button disabled={busy}>{busy ? 'Saving…' : selected ? 'Save changes' : 'Create workflow'}</button>{selected && <><button type="button" className="secondary" onClick={() => loadBuilder(null)}>Cancel</button><button type="button" className="danger" onClick={() => void deleteWorkflow()}>Delete</button></>}</div>
            </form>
            <div className="workflow-list">
              {workflows.length === 0 && <p className="muted">No workflows yet.</p>}
              {workflows.map((workflow) => <button className={`workflow-row ${selected?.id === workflow.id ? 'selected' : ''}`} key={workflow.id} onClick={() => void selectWorkflow(workflow)}><span>{workflow.name}</span><span className="status">{workflow.enabled ? 'ACTIVE' : 'DRAFT'}</span></button>)}
            </div>
          </section>
          <section className="card">
            <div className="detail-heading"><div><h2>{selected?.name ?? 'Select a workflow'}</h2><p className="muted">{selected ? `${selected.trigger.type} trigger · ${selected.actions[0]?.type ?? 'No'} action` : 'Configure a workflow to inspect it.'}</p></div>{selected && <button onClick={() => void runWorkflow()} disabled={busy}>Run now</button>}</div>
            <h3>Execution history</h3>
            {!selected && <p className="muted">Choose a workflow to inspect its runs.</p>}
            {selected && executions.length === 0 && <p className="muted">No executions recorded.</p>}
            {executions.map((execution) => <div className="execution-row" key={execution.id}><span>{execution.status}</span><code>{execution.id.slice(0, 8)}</code></div>)}
          </section>
        </div>
        {error && <p className="error">{error}</p>}
      </section>
    </main>
  )
}

export default App
