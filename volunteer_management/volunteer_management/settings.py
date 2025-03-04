"""
Django settings for volunteer_management project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i-=^x^=l)e@*4-4^gq%j9&6%)_%4+8iefo(j8#6#z#8tmi@*o('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.onrender.com']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'volunteer_management_app',
    'crispy_forms',
    'crispy_bootstrap5',
    'django.contrib.humanize',
    'django_ckeditor_5',
    'django_filters',
]

# Crispy forms configuration
CRISPY_TEMPLATE_PACK = 'bootstrap5'
CRISPY_FAIL_SILENTLY = not DEBUG

# CKEDITOR configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

customColorPalette = [
      {
          'color': 'hsl(4, 90%, 58%)',
          'label': 'Red'
      },
      {
          'color': 'hsl(340, 82%, 52%)',
          'label': 'Pink'
      },
      {
          'color': 'hsl(291, 64%, 42%)',
          'label': 'Purple'
      },
      {
          'color': 'hsl(262, 52%, 47%)',
          'label': 'Deep Purple'
      },
      {
          'color': 'hsl(231, 48%, 48%)',
          'label': 'Indigo'
      },
      {
          'color': 'hsl(207, 90%, 54%)',
          'label': 'Blue'
      },
  ]

CK_EDITOR_5_UPLOAD_FILE_VIEW_NAME = "custom_upload_file"
CKEDITOR_5_USER_LANGUAGE=True
CKEDITOR_5_CONFIGS = { 
  'default': {
      'toolbar': ['heading', '|', 'bold', 'italic', 'link',
                  'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],
      'language': 'vi',

  },
  'extends': {
      'blockToolbar': [
          'paragraph', 'heading1', 'heading2', 'heading3',
          '|',
          'bulletedList', 'numberedList',
          '|',
          'blockQuote',
      ],
      'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
      'code','subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
                  'bulletedList', 'numberedList', 'todoList', '|',  'blockQuote', 'imageUpload', '|',
                  'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
                  'insertTable',],
      'image': {
          'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                      'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side',  '|'],
          'styles': [
              'full',
              'side',
              'alignLeft',
              'alignRight',
              'alignCenter',
          ]

      },
      'table': {
          'contentToolbar': [ 'tableColumn', 'tableRow', 'mergeTableCells',
          'tableProperties', 'tableCellProperties' ],
          'tableProperties': {
              'borderColors': customColorPalette,
              'backgroundColors': customColorPalette
          },
          'tableCellProperties': {
              'borderColors': customColorPalette,
              'backgroundColors': customColorPalette
          }
      },
      'heading' : {
          'options': [
              { 'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph' },
              { 'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1' },
              { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2' },
              { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3' }
          ]
      }
  },
  'list': {
      'properties': {
          'styles': 'true',
          'startIndex': 'true',
          'reversed': 'true',
      }
  }
}

# Jazzmin configuration

JAZZMIN_SETTINGS = {
    # Tiêu đề của trang quản trị
    "site_title": "Quản lý Sự kiện Tình nguyện",
    "site_header": "Quản lý Sự kiện Tình nguyện",
    "site_brand": "Quản Lý Tình Nguyện IUH",

    # Logo (cần đặt file logo trong thư mục static)
    "site_logo": "images/Logo-IUH.jpg",

    # Thông báo chào mừng
    "welcome_sign": "Chào mừng đến với trang quản trị tình nguyện IUH",
            
    # Các model để tìm kiếm
    "search_model": [
        "volunteer_management_app.CustomUser",
        "volunteer_management_app.VolunteerEventPost",
        "volunteer_management_app.EventReport",
    ],

    # Không sử dụng avatar cho người dùng
    "user_avatar": "avatar",  # Default: "user

    # Liên kết menu trên cùng
    "topmenu_links": [
        {"name": "Trang chủ", "url": "/", "new_window": True},
    ],

    # Liên kết menu người dùng
    "usermenu_links": [

    ],

    # Hiển thị sidebar
    "show_sidebar": True,
    "navigation_expanded": True,

    # Thứ tự hiển thị các ứng dụng và model trong sidebar
    "order_with_respect_to": [
        "volunteer_management_app",
        "auth",
        "volunteer_management_app.customuser",
        "volunteer_management_app.adminuser",
        "volunteer_management_app.volunteereventpost",
        "volunteer_management_app.eventreport",
    ],

    # Định nghĩa các icon cho model
    "icons": {
        "dashboard": "fas fa-tachometer-alt",
        "volunteer_management_app.adminuser": "fas fa-user-tie",
        "volunteer_management_app.customuser": "fas fa-user",
        "volunteer_management_app.volunteereventpost": "fas fa-calendar-check",
        "volunteer_management_app.eventreport": "fas fa-file-alt",
        "auth.Group": "fas fa-users",
    },

    # Định dạng trang chi tiết (change view)
    "changeform_format": "single",
    "show_ui_builder": True,
    
    # Cấu hình CSS
    "custom_css": "css/admin.css",
    
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": True,
    "brand_colour": False,
    "accent": "accent-lightblue",
    "navbar": "navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-lightblue",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": True
}
  
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'volunteer_management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'volunteer_management.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'volunteer_management_app.CustomUser'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.RemoteUserBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'vi'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
