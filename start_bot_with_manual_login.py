#!/usr/bin/env python3
"""
Wrapper script per avviare il bot con login manuale assistito.
"""

import subprocess
import sys

print("=" * 70)
print("🤖 AUTO JOB APPLIER - AVVIO CON LOGIN MANUALE")
print("=" * 70)
print()
print("📋 ISTRUZIONI:")
print("1. Chrome si aprirà automaticamente")
print("2. Vai su LinkedIn e fai login manualmente")
print("3. Il bot partirà automaticamente dopo l'avvio")
print()
print("⚠️  NON CHIUDERE Chrome!")
print()
print("=" * 70)
print()
print("🚀 Avvio runAiBot.py...")
print()

try:
    subprocess.run([sys.executable, "runAiBot.py"], check=True)
except KeyboardInterrupt:
    print("\n⚠️  Bot interrotto dall'utente (CTRL+C)")
    sys.exit(0)
except Exception as e:
    print(f"\n❌ Errore: {e}")
    sys.exit(1)
