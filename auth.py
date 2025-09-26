from flask import Blueprint, jsonify, request
from src.services.auth_service import auth_service

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    """Doctor login endpoint"""
    try:
        data = request.json
        
        if not data or not all(key in data for key in ['username', 'password']):
            return jsonify({'error': 'Missing username or password'}), 400
        
        result = auth_service.authenticate(data['username'], data['password'])
        
        if result['success']:
            return jsonify({
                'success': True,
                'session_token': result['session_token'],
                'username': result['username'],
                'expires_at': result['expires_at']
            }), 200
        else:
            return jsonify({'error': result['message']}), 401
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth_bp.route('/validate', methods=['POST'])
def validate_session():
    """Validate session token"""
    try:
        data = request.json
        
        if not data or 'session_token' not in data:
            return jsonify({'error': 'Missing session token'}), 400
        
        result = auth_service.validate_session(data['session_token'])
        
        if result['valid']:
            return jsonify({
                'valid': True,
                'username': result['username']
            }), 200
        else:
            return jsonify({'valid': False, 'message': result['message']}), 401
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth_bp.route('/logout', methods=['POST'])
def logout():
    """Doctor logout endpoint"""
    try:
        data = request.json
        
        if not data or 'session_token' not in data:
            return jsonify({'error': 'Missing session token'}), 400
        
        success = auth_service.logout(data['session_token'])
        
        return jsonify({
            'success': success,
            'message': 'Logged out successfully' if success else 'Invalid session'
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
