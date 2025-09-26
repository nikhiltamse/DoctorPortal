import hashlib
import secrets
from datetime import datetime, timedelta

class AuthService:
    """
    Simple authentication service for doctors.
    In production, this would use proper password hashing and session management.
    """
    
    def __init__(self):
        # Simple in-memory storage for demo purposes
        # In production, this would be stored in database
        self.doctors = {
            'doctor': self._hash_password('password123'),  # username: doctor, password: password123
            'admin': self._hash_password('admin123')       # username: admin, password: admin123
        }
        self.active_sessions = {}  # session_token: {username, expires_at}
    
    def _hash_password(self, password: str) -> str:
        """Hash password using SHA-256 (in production, use bcrypt or similar)"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def authenticate(self, username: str, password: str) -> dict:
        """
        Authenticate doctor credentials
        
        Args:
            username: Doctor's username
            password: Doctor's password
            
        Returns:
            dict: Authentication result with session token if successful
        """
        if username not in self.doctors:
            return {'success': False, 'message': 'Invalid username or password'}
        
        hashed_password = self._hash_password(password)
        if self.doctors[username] != hashed_password:
            return {'success': False, 'message': 'Invalid username or password'}
        
        # Generate session token
        session_token = secrets.token_urlsafe(32)
        expires_at = datetime.utcnow() + timedelta(hours=8)  # 8 hour session
        
        self.active_sessions[session_token] = {
            'username': username,
            'expires_at': expires_at
        }
        
        return {
            'success': True,
            'session_token': session_token,
            'username': username,
            'expires_at': expires_at.isoformat()
        }
    
    def validate_session(self, session_token: str) -> dict:
        """
        Validate if session token is valid and not expired
        
        Args:
            session_token: Session token to validate
            
        Returns:
            dict: Validation result with user info if valid
        """
        if not session_token or session_token not in self.active_sessions:
            return {'valid': False, 'message': 'Invalid session token'}
        
        session = self.active_sessions[session_token]
        
        if datetime.utcnow() > session['expires_at']:
            # Session expired, remove it
            del self.active_sessions[session_token]
            return {'valid': False, 'message': 'Session expired'}
        
        return {
            'valid': True,
            'username': session['username']
        }
    
    def logout(self, session_token: str) -> bool:
        """
        Logout and invalidate session
        
        Args:
            session_token: Session token to invalidate
            
        Returns:
            bool: True if successfully logged out
        """
        if session_token in self.active_sessions:
            del self.active_sessions[session_token]
            return True
        return False
    
    def cleanup_expired_sessions(self):
        """Remove expired sessions from memory"""
        current_time = datetime.utcnow()
        expired_tokens = [
            token for token, session in self.active_sessions.items()
            if current_time > session['expires_at']
        ]
        
        for token in expired_tokens:
            del self.active_sessions[token]

# Global instance
auth_service = AuthService()
