import { useState } from 'react'
import type { FormEvent } from 'react'

type Message = {
  id: number
  text: string
}

function App() {
  // State to hold the list of messages & Values in text box
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState('')

  // Called when form is submitted or press Enter
  const handleSubmit = (e: FormEvent) => {
    e.preventDefault() // stop page reload

    const trimmed = input.trim()
    if (!trimmed) return // ignore empty messages

    const newMessage: Message = {
      id: Date.now(),
      text: trimmed,
    }

    // Append new message to list
    setMessages(prev => [...prev, newMessage])

    //Clear input box
    setInput('')
  }

  return (
    <div
      style={{
        minHeight: '100vh',
        backgroundColor: '#020617',
        color: '#e5e7eb',
        fontFamily: 'system-ui, -apple-system, BlinkMacSystemFont, sans-serif',
        display: 'flex',
        flexDirection: 'column',
        // ⬇️ extra bottom padding so the input isn't flush with the screen edge
        padding: '1.5rem 1.5rem 3rem',
        boxSizing: 'border-box',
      }}
    >
      {/* Header */}
      <header style={{ marginBottom: '1rem' }}>
        <h1 style={{ fontSize: '1.75rem', marginBottom: '0.25rem' }}>🧠 Homebrain</h1>
        <p style={{ opacity: 0.8, fontSize: '0.9rem' }}>
          Central Homelab Knowledge ⚪ AI assistant
        </p>
      </header>

      {/* Chat container */}
      <div
        style={{
          flex: 1,
          display: 'flex',
          flexDirection: 'column',
          borderRadius: '0.75rem',
          border: '1px solid #1f2937',
          backgroundColor: '#020617',
          padding: '0.75rem',
        }}
      >
        {/* Scrollable messages */}
        <div
          style={{
            flex: 1,
            overflowY: 'auto',
            display: 'flex',
            flexDirection: 'column',
            gap: '0.5rem',
            paddingBottom: '0.5rem',
          }}
        >
          {messages.length === 0 ? (
            <span style={{ opacity: 0.7, fontSize: '0.9rem' }}>
              No messages yet. Type something below to get started.
            </span>
          ) : (
            messages.map(message => (
              <div
                key={message.id}
                style={{
                  alignSelf: 'flex-start',
                  padding: '0.5rem 0.75rem',
                  borderRadius: '0.5rem',
                  backgroundColor: '#0b1120',
                  border: '1px solid #1f2937',
                  fontSize: '0.9rem',
                }}
              >
                {message.text}
              </div>
            ))
          )}
        </div>

        {/* Input bar */}
        <form
          onSubmit={handleSubmit}
          style={{
            borderTop: '1px solid #1f2937',
            paddingTop: '0.5rem',
            display: 'flex',
            gap: '0.5rem',
            marginTop: '0.5rem',
          }}
        >
          <input
            type="text"
            value={input}
            onChange={event => setInput(event.target.value)}
            placeholder="Type a message..."
            style={{
              flex: 1,
              padding: '0.5rem 0.75rem',
              borderRadius: '0.5rem',
              border: '1px solid #374151',
              backgroundColor: '#020617',
              color: '#e5e7eb',
              fontSize: '0.9rem',
            }}
          />
          <button
            type="submit"
            style={{
              padding: '0.5rem 0.9rem',
              borderRadius: '0.5rem',
              border: 'none',
              fontWeight: 500,
              cursor: 'pointer',
              backgroundColor: '#22c55e',
              color: '#022c22',
              fontSize: '0.9rem',
            }}
          >
            Send
          </button>
        </form>
      </div>
    </div>
  )
}

export default App
