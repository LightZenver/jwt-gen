#!/usr/bin/env python3
"""
JWT Key Generator Control Panel
Interactive control panel for JWT key generation
"""

import os
import json
import subprocess
import sys
from datetime import datetime

class ControlPanel:
    def __init__(self):
        self.settings_file = 'panel_settings.json'
        self.config_file = 'config.json'
        self.settings = self.load_default_settings()
        self.load_settings()

    def load_default_settings(self):
        """Load default settings"""
        return {
            'output_dir': 'generated_keys',
            'key_prefix': 'jwt_keys',
            'algorithms': ['HMAC', 'RSA', 'EC'],
            'hmac_bits': 256,
            'rsa_key_size': 2048,
            'token_expiry': 24,
            'generate_examples': True
        }

    def clear_screen(self):
        """Clear screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self):
        """Print header"""
        self.clear_screen()
        print("🎛️" + "="*60)
        print("           JWT KEY GENERATOR CONTROL PANEL v2.1")
        print("="*60)
        print("           🔐 JWT Key Generation Control Panel")
        print("="*60)

    def load_settings(self):
        """Load settings from file"""
        try:
            if os.path.exists(self.settings_file):
                with open(self.settings_file, 'r', encoding='utf-8') as f:
                    saved_settings = json.load(f)
                    self.settings.update(saved_settings)
                print(f"✅ Settings loaded from {self.settings_file}")
        except Exception as e:
            print(f"⚠️ Error loading settings: {e}")

    def save_settings(self):
        """Save settings to file"""
        try:
            with open(self.settings_file, 'w', encoding='utf-8') as f:
                json.dump(self.settings, f, indent=2, ensure_ascii=False)
            print(f"✅ Panel settings saved to {self.settings_file}")
            
            # UPDATE GENERATOR CONFIG
            self.update_generator_config()
            return True
        except Exception as e:
            print(f"❌ Error saving settings: {e}")
            return False

    def update_generator_config(self):
        """Update generator configuration file"""
        config = {
            'output_dir': self.settings['output_dir'],
            'output_prefix': self.settings['key_prefix'],
            'key_size': self.settings['rsa_key_size'],
            'token_expiry_hours': self.settings['token_expiry'],
            'generate_examples': self.settings['generate_examples']
        }
        
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            print(f"✅ Generator config updated: {self.config_file}")
        except Exception as e:
            print(f"❌ Error updating generator config: {e}")

    def show_main_menu(self):
        """Main menu"""
        while True:
            self.print_header()
            print("\n📋 MAIN MENU:")
            print("1. ⚙️  Generation Settings")
            print("2. 🚀 Start Key Generation")
            print("3. 📊 View Current Settings") 
            print("4. 💾 Save Settings")
            print("5. 📥 Load Default Settings")
            print("6. 🚪 Exit")
            print("\n" + "="*60)

            choice = input("Choose action [1-6]: ").strip()

            if choice == '1':
                self.settings_menu()
            elif choice == '2':
                self.start_generation()
            elif choice == '3':
                self.show_current_settings()
            elif choice == '4':
                if self.save_settings():
                    input("✅ All settings saved! Press Enter...")
            elif choice == '5':
                self.settings = self.load_default_settings()
                self.save_settings()
                input("✅ Settings reset to defaults! Press Enter...")
            elif choice == '6':
                # Auto-save on exit
                self.save_settings()
                print("👋 Goodbye!")
                break
            else:
                input("❌ Invalid choice! Press Enter...")

    def settings_menu(self):
        """Settings menu"""
        while True:
            self.print_header()
            print("\n⚙️  GENERATION SETTINGS:")
            print(f"1. 📁 Output Directory: {self.settings['output_dir']}")
            print(f"2. 🏷️  File Prefix: {self.settings['key_prefix']}")
            print(f"3. 🔑 Algorithms: {', '.join(self.settings['algorithms'])}")
            print(f"4. 🔢 HMAC Key Size: {self.settings['hmac_bits']} bits")
            print(f"5. 🗝️  RSA Key Size: {self.settings['rsa_key_size']} bits")
            print(f"6. ⏰ Token Expiry: {self.settings['token_expiry']} hours")
            print(f"7. 📝 Generate Examples: {'Yes' if self.settings['generate_examples'] else 'No'}")
            print("8. 💾 Save and Apply")
            print("9. ↩️  Back to Main Menu")
            print("\n" + "="*60)

            choice = input("Choose setting [1-9]: ").strip()

            if choice == '1':
                new_dir = input(f"Output directory [{self.settings['output_dir']}]: ").strip()
                if new_dir:
                    self.settings['output_dir'] = new_dir
                    print(f"✅ Directory set to: {new_dir}")
            elif choice == '2':
                new_prefix = input(f"File prefix [{self.settings['key_prefix']}]: ").strip()
                if new_prefix:
                    self.settings['key_prefix'] = new_prefix
                    print(f"✅ Prefix set to: {new_prefix}")
            elif choice == '3':
                self.algorithm_selection()
            elif choice == '4':
                self.hmac_settings()
            elif choice == '5':
                self.rsa_settings()
            elif choice == '6':
                self.token_settings()
            elif choice == '7':
                self.settings['generate_examples'] = not self.settings['generate_examples']
                status = "enabled" if self.settings['generate_examples'] else "disabled"
                print(f"✅ Example generation: {status}")
            elif choice == '8':
                if self.save_settings():
                    input("✅ Settings saved and applied! Press Enter...")
                else:
                    input("❌ Save error! Press Enter...")
            elif choice == '9':
                break
            else:
                input("❌ Invalid choice! Press Enter...")

    def algorithm_selection(self):
        """Algorithm selection"""
        while True:
            self.print_header()
            print("\n🔑 ALGORITHM SELECTION:")
            algorithms_status = ", ".join(self.settings['algorithms']) if self.settings['algorithms'] else "NONE"
            print(f"Current selection: {algorithms_status}")
            print("\n1. 🔄 HMAC - " + ("✅" if 'HMAC' in self.settings['algorithms'] else "❌"))
            print("2. 🔄 RSA - " + ("✅" if 'RSA' in self.settings['algorithms'] else "❌")) 
            print("3. 🔄 EC - " + ("✅" if 'EC' in self.settings['algorithms'] else "❌"))
            print("4. ✅ Select All Algorithms")
            print("5. ❌ Clear All")
            print("6. 💾 Apply Selection")
            print("7. ↩️  Back")
            print("\n" + "="*60)

            choice = input("Choose action [1-7]: ").strip()

            if choice == '1':
                self.toggle_algorithm('HMAC')
            elif choice == '2':
                self.toggle_algorithm('RSA')
            elif choice == '3':
                self.toggle_algorithm('EC')
            elif choice == '4':
                self.settings['algorithms'] = ['HMAC', 'RSA', 'EC']
                print("✅ All algorithms selected")
            elif choice == '5':
                self.settings['algorithms'] = []
                print("✅ All algorithms disabled")
            elif choice == '6':
                print("✅ Algorithm selection applied")
                break
            elif choice == '7':
                break
            else:
                input("❌ Invalid choice! Press Enter...")

    def toggle_algorithm(self, algorithm):
        """Toggle algorithm"""
        if algorithm in self.settings['algorithms']:
            self.settings['algorithms'].remove(algorithm)
            print(f"❌ {algorithm} disabled")
        else:
            self.settings['algorithms'].append(algorithm)
            print(f"✅ {algorithm} enabled")

    def hmac_settings(self):
        """HMAC settings"""
        while True:
            self.print_header()
            print("\n🔢 HMAC SETTINGS:")
            print(f"Current size: {self.settings['hmac_bits']} bits")
            print("\nAvailable sizes:")
            print(f"1. 256 bits (HS256) {'✅' if self.settings['hmac_bits'] == 256 else ''}")
            print(f"2. 384 bits (HS384) {'✅' if self.settings['hmac_bits'] == 384 else ''}")
            print(f"3. 512 bits (HS512) {'✅' if self.settings['hmac_bits'] == 512 else ''}")
            print("4. ↩️ Back")

            choice = input("Choose size [1-4]: ").strip()
            bits_map = {'1': 256, '2': 384, '3': 512}
            
            if choice in bits_map:
                self.settings['hmac_bits'] = bits_map[choice]
                print(f"✅ Size set to: {bits_map[choice]} bits")
                break
            elif choice == '4':
                break
            else:
                input("❌ Invalid choice! Press Enter...")

    def rsa_settings(self):
        """RSA settings"""
        while True:
            self.print_header()
            print("\n🗝️  RSA SETTINGS:")
            print(f"Current size: {self.settings['rsa_key_size']} bits")
            print("\nAvailable sizes:")
            print(f"1. 2048 bits {'✅' if self.settings['rsa_key_size'] == 2048 else ''}")
            print(f"2. 3072 bits {'✅' if self.settings['rsa_key_size'] == 3072 else ''}")
            print(f"3. 4096 bits {'✅' if self.settings['rsa_key_size'] == 4096 else ''}")
            print("4. ↩️ Back")

            choice = input("Choose size [1-4]: ").strip()
            size_map = {'1': 2048, '2': 3072, '3': 4096}
            
            if choice in size_map:
                self.settings['rsa_key_size'] = size_map[choice]
                print(f"✅ Size set to: {size_map[choice]} bits")
                break
            elif choice == '4':
                break
            else:
                input("❌ Invalid choice! Press Enter...")

    def token_settings(self):
        """Token settings"""
        self.print_header()
        print("\n⏰ TOKEN SETTINGS:")
        print(f"Current expiry: {self.settings['token_expiry']} hours")
        
        try:
            new_expiry = input("New expiry (in hours): ").strip()
            if new_expiry:
                expiry = int(new_expiry)
                if 1 <= expiry <= 8760:
                    self.settings['token_expiry'] = expiry
                    print(f"✅ Expiry set to: {expiry} hours")
                else:
                    input("❌ Expiry must be between 1 and 8760 hours!")
        except ValueError:
            input("❌ Please enter a valid number!")

    def show_current_settings(self):
        """Show current settings"""
        self.print_header()
        print("\n📊 CURRENT SETTINGS:")
        print(f"📁 Output Directory: {self.settings['output_dir']}")
        print(f"🏷️  File Prefix: {self.settings['key_prefix']}")
        print(f"🔑 Algorithms: {', '.join(self.settings['algorithms']) or 'None'}")
        print(f"🔢 HMAC Size: {self.settings['hmac_bits']} bits")
        print(f"🗝️  RSA Size: {self.settings['rsa_key_size']} bits")
        print(f"⏰ Token Expiry: {self.settings['token_expiry']} hours")
        print(f"📝 Generate Examples: {'Yes' if self.settings['generate_examples'] else 'No'}")
        
        # Show file status
        print(f"\n💾 Configuration Files:")
        print(f"   Panel: {'✅' if os.path.exists(self.settings_file) else '❌'} {self.settings_file}")
        print(f"   Generator: {'✅' if os.path.exists(self.config_file) else '❌'} {self.config_file}")
        
        input("\nPress Enter to continue...")

    def start_generation(self):
        """Start key generation"""
        if not self.settings['algorithms']:
            input("❌ No algorithms selected for generation! Press Enter...")
            return

        # UPDATE CONFIG BEFORE GENERATION
        if not self.save_settings():
            input("❌ Error saving settings! Generation cancelled.")
            return

        self.print_header()
        print("\n🚀 STARTING KEY GENERATION")
        print("="*60)
        
        print("📋 Generation Parameters:")
        print(f"   📁 Directory: {self.settings['output_dir']}")
        print(f"   🏷️  Prefix: {self.settings['key_prefix']}")
        print(f"   🔑 Algorithms: {', '.join(self.settings['algorithms'])}")
        print(f"   🔢 HMAC: {self.settings['hmac_bits']} bits")
        print(f"   🗝️  RSA: {self.settings['rsa_key_size']} bits")
        print(f"   📝 Examples: {'Yes' if self.settings['generate_examples'] else 'No'}")
        print("\n" + "="*60)

        confirm = input("✅ Start generation? (y/N): ").strip().lower()
        if confirm != 'y':
            return

        print("\n🔄 Launching generator...")
        print("="*60)

        # Build command
        cmd = [sys.executable, "jwtgen.py"]
        
        # Add parameters from settings
        cmd.extend(["--output", self.settings['key_prefix']])
        
        # Add algorithm flags
        algorithms = self.settings['algorithms']
        if len(algorithms) == 1:
            if 'HMAC' in algorithms:
                cmd.append("--hmac-only")
            elif 'RSA' in algorithms:
                cmd.append("--rsa-only")
            elif 'EC' in algorithms:
                cmd.append("--ec-only")
        
        # Add examples flag
        if not self.settings['generate_examples']:
            cmd.append("--no-examples")

        try:
            # Show command
            print(f"🔧 Command: {' '.join(cmd)}")
            print("="*60)
            
            # Run generator
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            print("✅ Generation completed successfully!")
            if result.stdout:
                print(result.stdout)
            
        except subprocess.CalledProcessError as e:
            print("❌ Error during key generation!")
            print(f"Error code: {e.returncode}")
            if e.stderr:
                print(f"Error: {e.stderr}")
        except FileNotFoundError:
            print("❌ jwtgen.py file not found!")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

        input("\nPress Enter to return to menu...")

def main():
    """Main function"""
    try:
        panel = ControlPanel()
        # Create initial config if missing
        if not os.path.exists(panel.config_file):
            panel.save_settings()
        panel.show_main_menu()
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted by user")
    except Exception as e:
        print(f"❌ Critical error: {e}")
        import traceback
        traceback.print_exc()
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
