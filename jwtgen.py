#!/usr/bin/env python3
"""
JWT Key Generator Core
JWT key generation core – called from the control panel
"""

import json
import base64
import secrets
import os
from datetime import datetime, timedelta
import argparse
import sys

try:
    import jwt
except ImportError:
    print("❌ Error: PyJWT library is not installed")
    sys.exit(1)

try:
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric import rsa, ec
    from cryptography.hazmat.backends import default_backend
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

class JWTGeneratorCore:
    def __init__(self):
        self.config = self.load_config()

    def load_config(self, config_file='config.json'):
        """Load configuration"""
        default_config = {
            'output_dir': 'generated_keys',
            'output_prefix': 'jwt_keys', 
            'key_size': 2048,
            'token_expiry_hours': 24,
            'generate_examples': True
        }
        
        try:
            if os.path.exists(config_file):
                with open(config_file, 'r', encoding='utf-8') as f:
                    loaded_config = json.load(f)
                    default_config.update(loaded_config)
                print(f"✅ Configuration loaded: {config_file}")
        except Exception as e:
            print(f"⚠️ Error loading config: {e}")
            
        return default_config

    def generate_hmac_secret(self, bits=256):
        """Generate HMAC secret"""
        secret = secrets.token_bytes(bits // 8)
        return base64.urlsafe_b64encode(secret).decode('utf-8')

    def generate_rsa_keys(self, key_size=2048):
        """Generate RSA keys"""
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=default_backend()
        )
        
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ).decode('utf-8')
        
        public_key = private_key.public_key()
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')
        
        return private_pem, public_pem

    def generate_ec_keys(self):
        """Generate EC keys"""
        private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
        
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ).decode('utf-8')
        
        public_key = private_key.public_key()
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')
        
        return private_pem, public_pem

    def create_example_token(self, hmac_secret, output_dir, prefix, timestamp):
        """Create example token"""
        if not self.config.get('generate_examples', True):
            print("ℹ️  Example generation is disabled in settings")
            return
            
        example_file = os.path.join(output_dir, f"{prefix}_example_{timestamp}.json")
        
        payload = {
            'iss': 'jwt-key-generator',
            'sub': 'test_user',
            'aud': 'api.example.com', 
            'iat': datetime.utcnow().timestamp(),
            'exp': (datetime.utcnow() + timedelta(hours=self.config['token_expiry_hours'])).timestamp(),
            'jti': secrets.token_hex(16),
            'data': {
                'user_id': 12345,
                'username': 'test_user',
                'email': 'user@example.com',
                'roles': ['user', 'admin']
            }
        }
        
        token = jwt.encode(payload, hmac_secret, algorithm='HS256')
        
        try:
            verified = jwt.decode(token, hmac_secret, algorithms=['HS256'])
            valid = True
        except jwt.InvalidTokenError:
            verified = "Invalid token"
            valid = False
        
        example_data = {
            'algorithm': 'HS256',
            'secret_key': hmac_secret,
            'payload': payload,
            'jwt_token': token,
            'verification_result': valid,
            'decoded_payload': verified if valid else verified
        }
        
        with open(example_file, 'w', encoding='utf-8') as f:
            json.dump(example_data, f, indent=2, default=str, ensure_ascii=False)
        
        print(f"✅ Example token: {example_file}")

    def generate_all_keys(self):
        """Generate all keys"""
        results = {}
        
        # HMAC keys
        print("🔑 Generating HMAC keys...")
        results['hmac'] = {
            'HS256': self.generate_hmac_secret(256),
            'HS384': self.generate_hmac_secret(384), 
            'HS512': self.generate_hmac_secret(512)
        }
        
        # RSA keys
        if CRYPTO_AVAILABLE:
            print("🔐 Generating RSA keys...")
            rsa_private, rsa_public = self.generate_rsa_keys(self.config['key_size'])
            results['rsa'] = {
                'private_key': rsa_private,
                'public_key': rsa_public
            }
            
            # EC keys
            print("🔒 Generating EC keys...")
            ec_private, ec_public = self.generate_ec_keys()
            results['ec'] = {
                'private_key': ec_private,
                'public_key': ec_public
            }
        
        return results

    def save_keys(self, keys, prefix=None):
        """Save keys to files"""
        if prefix is None:
            prefix = self.config['output_prefix']
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = self.config['output_dir']
        
        # Create directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        print(f"📁 Output directory: {output_dir}")
        
        # Save HMAC
        if 'hmac' in keys:
            hmac_file = os.path.join(output_dir, f"{prefix}_hmac_{timestamp}.json")
            with open(hmac_file, 'w', encoding='utf-8') as f:
                json.dump(keys['hmac'], f, indent=2, ensure_ascii=False)
            print(f"✅ HMAC keys: {hmac_file}")
            
            # Create example token
            self.create_example_token(keys['hmac']['HS256'], output_dir, prefix, timestamp)
        
        # Save RSA
        if 'rsa' in keys:
            priv_file = os.path.join(output_dir, f"{prefix}_rsa_private_{timestamp}.pem")
            pub_file = os.path.join(output_dir, f"{prefix}_rsa_public_{timestamp}.pem")
            
            with open(priv_file, 'w', encoding='utf-8') as f:
                f.write(keys['rsa']['private_key'])
            with open(pub_file, 'w', encoding='utf-8') as f:
                f.write(keys['rsa']['public_key'])
                
            print(f"✅ RSA private key: {priv_file}")
            print(f"✅ RSA public key: {pub_file}")
        
        # Save EC
        if 'ec' in keys:
            priv_file = os.path.join(output_dir, f"{prefix}_ec_private_{timestamp}.pem")
            pub_file = os.path.join(output_dir, f"{prefix}_ec_public_{timestamp}.pem")
            
            with open(priv_file, 'w', encoding='utf-8') as f:
                f.write(keys['ec']['private_key'])
            with open(pub_file, 'w', encoding='utf-8') as f:
                f.write(keys['ec']['public_key'])
                
            print(f"✅ EC private key: {priv_file}")
            print(f"✅ EC public key: {pub_file}")

def main():
    parser = argparse.ArgumentParser(description='JWT Key Generator Core')
    parser.add_argument('--output', '-o', help='File prefix')
    parser.add_argument('--hmac-only', action='store_true', help='HMAC only')
    parser.add_argument('--rsa-only', action='store_true', help='RSA only') 
    parser.add_argument('--ec-only', action='store_true', help='EC only')
    parser.add_argument('--no-examples', action='store_true', help='Do not generate examples')
    
    args = parser.parse_args()
    
    generator = JWTGeneratorCore()
    
    # Override settings from arguments
    if args.no_examples:
        generator.config['generate_examples'] = False
    
    try:
        if args.hmac_only:
            print("🔑 Generating HMAC keys...")
            keys = {
                'hmac': {
                    'HS256': generator.generate_hmac_secret(256),
                    'HS384': generator.generate_hmac_secret(384),
                    'HS512': generator.generate_hmac_secret(512)
                }
            }
        elif args.rsa_only:
            if not CRYPTO_AVAILABLE:
                print("❌ Cryptography is not installed")
                sys.exit(1)
            print("🔐 Generating RSA keys...")
            rsa_priv, rsa_pub = generator.generate_rsa_keys(generator.config['key_size'])
            keys = {'rsa': {'private_key': rsa_priv, 'public_key': rsa_pub}}
        elif args.ec_only:
            if not CRYPTO_AVAILABLE:
                print("❌ Cryptography is not installed")
                sys.exit(1)
            print("🔒 Generating EC keys...")
            ec_priv, ec_pub = generator.generate_ec_keys()
            keys = {'ec': {'private_key': ec_priv, 'public_key': ec_pub}}
        else:
            keys = generator.generate_all_keys()
        
        generator.save_keys(keys, args.output)
        print("\n🎉 Generation completed successfully!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
