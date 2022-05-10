import sys
import ctypes
import subprocess
import os

def main():
    if os.path.isdir(r"C:\Program Files\WinRAR"):
        file = open(r"C:\Program Files\WinRAR\rarreg.key", 'w')
        file.write(("""RAR registration data\nHardik\nwww.Hardik.live\nUID=448c4a899c6cdc1039c5\n641221225039c585fc5ef8da12ccf689780883109587752a828ff0\n59ae0579fe68942c97d160f361d16f96c8fe03f1f89c66abc25a37\n7777a27ec82f103b3d8e05dcefeaa45c71675ca822242858a1c897\nc57d0b0a3fe7ac36c517b1d2be385dcc726039e5f536439a806c35\n1e180e47e6bf51febac6eaae111343d85015dbd59ba45c71675ca8\n2224285927550547c74c826eade52bbdb578741acc1565af60e326\n6b5e5eaa169647277b533e8c4ac01535547d1dee14411061928023""").strip())
        
if __name__ == "__main__":
    if ctypes.windll.shell32.IsUserAnAdmin() == False:
        print("I must be ran as administrator or I can't apply changes.")
        
        if input("Restart as admin (yes/no)? ") == "yes":
            subprocess.run(["powershell.exe", "Start-Process '.\winrar-activator.exe' -Verb runAs"], stderr=None)
            
        sys.exit()
        
    main()