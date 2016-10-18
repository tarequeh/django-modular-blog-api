"""
Values that are used throughout the app
"""

FRAGMENT_TYPE_PLAINTEXT = 'plaintext'
FRAGMENT_TYPE_HTML = 'html'
FRAGMENT_TYPE_MARKDOWN = 'markdown'
FRAGMENT_TYPE_IMAGE = 'image'
FRAGMENT_TYPE_CODE = 'code'
FRAGMENT_TYPE_EMBED = 'embed'

FRAGMENT_TYPE_CHOICES = (
    (FRAGMENT_TYPE_PLAINTEXT, 'Plaintext'),
    (FRAGMENT_TYPE_HTML, 'HTML'),
    (FRAGMENT_TYPE_MARKDOWN, 'Markdown'),
    (FRAGMENT_TYPE_IMAGE, 'Image'),
    (FRAGMENT_TYPE_CODE, 'Code'),
    (FRAGMENT_TYPE_EMBED, 'Embed'),
)


CODE_LANGUAGE_GENERIC = 'generic'
CODE_LANGUAGE_PYTHON = 'python'
CODE_LANGUAGE_BASH = 'bash'
CODE_LANGUAGE_JAVASCRIPT = 'javascript'
CODE_LANGUAGE_HTML = 'html'
CODE_LANGUAGE_CSS = 'css'

CODE_LANGUAGE_CHOICES = (
    (CODE_LANGUAGE_GENERIC, 'Generic'),
    (CODE_LANGUAGE_PYTHON, 'Python'),
    (CODE_LANGUAGE_BASH, 'Bash'),
    (CODE_LANGUAGE_JAVASCRIPT, 'JavaScript'),
    (CODE_LANGUAGE_HTML, 'HTML'),
    (CODE_LANGUAGE_CSS, 'CSS'),
)

EMBED_TYPE_RAW = 'raw'
EMBED_TYPE_VIMEO = 'vimeo'
EMBED_TYPE_YOUTUBE = 'youtube'
EMBED_TYPE_TWEET = 'tweet'
EMBED_TYPE_INSTAGRAM = 'instagram'

EMBED_TYPE_CHOICES = (
    (EMBED_TYPE_RAW, 'Raw'),
    (EMBED_TYPE_VIMEO, 'Vimeo'),
    (EMBED_TYPE_YOUTUBE, 'Youtube'),
    (EMBED_TYPE_TWEET, 'Tweet'),
    (EMBED_TYPE_INSTAGRAM, 'Instagram'),
)

POST_STATE_DRAFT = 'draft'
POST_STATE_PUBLISHED = 'published'
POST_STATE_ARCHIVED = 'archived'
POST_STATE_CHOICES = (
    (POST_STATE_DRAFT, 'Draft'),
    (POST_STATE_PUBLISHED, 'Published'),
    (POST_STATE_ARCHIVED, 'Archived'),
)