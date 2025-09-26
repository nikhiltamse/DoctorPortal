from flask import Blueprint, jsonify, request
from src.services.medicine_templates import medicine_templates_service

templates_bp = Blueprint('templates', __name__)

@templates_bp.route('/templates', methods=['GET'])
def get_all_templates():
    """Get all available medicine templates"""
    try:
        templates = medicine_templates_service.get_all_templates()
        return jsonify(templates), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@templates_bp.route('/templates/<template_id>', methods=['GET'])
def get_template(template_id):
    """Get a specific template by ID"""
    try:
        template = medicine_templates_service.get_template(template_id)
        
        if template is None:
            return jsonify({'error': 'Template not found'}), 404
        
        return jsonify(template), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@templates_bp.route('/templates/search', methods=['GET'])
def search_templates():
    """Search templates by query"""
    try:
        query = request.args.get('q', '').strip()
        
        if not query:
            return jsonify({'error': 'Search query is required'}), 400
        
        results = medicine_templates_service.search_templates(query)
        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
