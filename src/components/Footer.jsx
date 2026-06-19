import React from 'react'
import { Link } from 'react-router-dom'
import { Shield, Github, Twitter, Linkedin, Heart } from 'lucide-react'

export default function Footer() {
  return (
    <footer className="border-t border-white/5 bg-[#0A1020]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-10">
          {/* Brand */}
          <div className="md:col-span-2">
            <Link to="/" className="flex items-center gap-2.5 mb-4">
              <div className="w-8 h-8 bg-blue-500 rounded-lg flex items-center justify-center" style={{boxShadow: '0 0 12px rgba(59,130,246,0.4)'}}>
                <Shield className="w-5 h-5 text-white" />
              </div>
              <span className="text-white font-bold text-lg">TrustShield <span className="text-blue-400">AI</span></span>
            </Link>
            <p className="text-slate-400 text-sm mb-2 font-mono tracking-widest uppercase">Analyze. Verify. Trust.</p>
            <p className="text-slate-500 text-sm leading-relaxed max-w-xs">
              Empowering individuals and organizations with AI-driven trust assessment for safer digital communication.
            </p>
            <div className="flex items-center gap-3 mt-5">
              {[Github, Twitter, Linkedin].map((Icon, i) => (
                <button key={i} className="w-8 h-8 rounded-lg bg-white/5 border border-white/10 flex items-center justify-center text-slate-400 hover:text-blue-400 hover:border-blue-500/30 transition-all duration-200">
                  <Icon className="w-4 h-4" />
                </button>
              ))}
            </div>
          </div>

          {/* Nav */}
          <div>
            <h4 className="text-white font-semibold text-sm mb-4">Platform</h4>
            <ul className="space-y-2">
              {[['/', 'Home'], ['/analyzer', 'Analyzer'], ['/dashboard', 'Dashboard'], ['/about', 'About']].map(([path, label]) => (
                <li key={path}>
                  <Link to={path} className="text-slate-400 hover:text-blue-400 text-sm transition-colors duration-200">
                    {label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          {/* Tech */}
          <div>
            <h4 className="text-white font-semibold text-sm mb-4">Built With</h4>
            <ul className="space-y-2">
              {['React.js', 'Tailwind CSS', 'Machine Learning', 'OCR Technology', 'SQL','LLM-Powered Analysis (Soon)' ].map(tech => (
                <li key={tech} className="text-slate-400 text-sm">{tech}</li>
              ))}
            </ul>
          </div>
        </div>

        <div className="mt-10 pt-8 border-t border-white/5 flex flex-col sm:flex-row items-center justify-between gap-4">
          <p className="text-slate-500 text-sm">
            © 2025 TrustShield AI.
          </p>
          <p className="text-slate-500 text-sm flex items-center gap-1.5">
            Built with <Heart className="w-3.5 h-3.5 text-red-400 fill-red-400" /> for safer digital communications
          </p>
        </div>
      </div>
    </footer>
  )
}
