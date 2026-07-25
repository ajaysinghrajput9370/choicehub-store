import os
from app import app, db, User
from werkzeug.security import generate_password_hash

def create_admin():
    with app.app_context():
        # Environment variables से admin credentials लें (Render पर डालें)
        admin_phone = os.environ.get('ADMIN_PHONE', '9999999999')
        admin_password = os.environ.get('ADMIN_PASSWORD', 'admin123')
        admin_email = os.environ.get('ADMIN_EMAIL', 'admin@choicehub.com')

        # Check if admin already exists
        existing = User.query.filter_by(role='admin').first()
        if existing:
            print(f"✅ Admin already exists: {existing.phone}")
            return

        admin = User(
            name='Super Admin',
            phone=admin_phone,
            email=admin_email,
            password_hash=generate_password_hash(admin_password),
            role='admin',
            referral_code='ADMIN001'
        )
        db.session.add(admin)
        db.session.commit()
        print(f"✅ Admin created with phone: {admin_phone}")

if __name__ == '__main__':
    create_admin()
