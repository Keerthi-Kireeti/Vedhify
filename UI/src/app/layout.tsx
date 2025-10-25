import React from 'react'
import { createRoot } from 'react-dom/client'
import { render } from 'react-dom'
import { BrowserRouter } from 'react-router-dom'
import { Provider } from 'react-redux'
import { store } from './store'
import { RootLayout } from './RootLayout'
import { App } from './App'
import './globals.css'

export const metadata = {
  title: 'Vedhify',
  description: 'Vedhify UI',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        {/* animated background shapes */}
        <div className="bg-shape" aria-hidden>
          <span></span>
          <span></span>
        </div>

        {children}
      </body>
    </html>
  )
}

export function App() {
  const root = createRoot(document.getElementById('root') as HTMLDivElement)
  return root.render(
    <Provider store={store}>
      <BrowserRouter>
        <RootLayout>
          <App />
        </RootLayout>
      </BrowserRouter>
    </Provider>
  )
}