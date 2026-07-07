from copy import deepcopy

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.colors import HexColor

# ==========================================================
# COLORS
# ==========================================================

PRIMARY = HexColor("#163A70")
LINK = HexColor("#0A66C2")
TEXT = HexColor("#222222")
SUBTEXT = HexColor("#555555")
LINE = HexColor("#D9D9D9")
DATE = HexColor("#777777")

# ==========================================================
# FONT SIZES
# ==========================================================

NAME_SIZE = 24
TITLE_SIZE = 11
SECTION_SIZE = 13
COMPANY_SIZE = 11
BODY_SIZE = 10
CONTACT_SIZE = 10

# ==========================================================
# SPACING
# ==========================================================

SPACE_SMALL = 4
SPACE_MEDIUM = 8
SPACE_LARGE = 12

# ==========================================================
# BASE STYLES
# ==========================================================

styles = getSampleStyleSheet()

# ==========================================================
# NAME
# ==========================================================

name_style = deepcopy(styles["Heading1"])
name_style.fontName = "Helvetica-Bold"
name_style.fontSize = NAME_SIZE
name_style.leading = 28
name_style.alignment = TA_CENTER
name_style.textColor = TEXT

# ==========================================================
# PROFILE TITLE
# ==========================================================

title_style = deepcopy(styles["BodyText"])
title_style.fontName = "Helvetica-Bold"
title_style.fontSize = TITLE_SIZE
title_style.leading = 14
title_style.alignment = TA_CENTER
title_style.textColor = SUBTEXT

# ==========================================================
# CONTACT
# ==========================================================

contact_style = deepcopy(styles["BodyText"])
contact_style.fontName = "Helvetica"
contact_style.fontSize = CONTACT_SIZE
contact_style.leading = 14
contact_style.alignment = TA_CENTER
contact_style.textColor = TEXT

# ==========================================================
# SECTION
# ==========================================================

section_style = deepcopy(styles["Heading2"])
section_style.fontName = "Helvetica-Bold"
section_style.fontSize = SECTION_SIZE
section_style.leading = 16
section_style.alignment = TA_LEFT
section_style.textColor = PRIMARY

# ==========================================================
# COMPANY
# ==========================================================

company_style = deepcopy(styles["BodyText"])
company_style.fontName = "Helvetica-Bold"
company_style.fontSize = COMPANY_SIZE
company_style.leading = 14
company_style.alignment = TA_LEFT
company_style.textColor = TEXT

# ==========================================================
# JOB TITLE
# ==========================================================

job_style = deepcopy(styles["BodyText"])
job_style.fontName = "Helvetica-Oblique"
job_style.fontSize = BODY_SIZE
job_style.leading = 13
job_style.alignment = TA_LEFT
job_style.textColor = SUBTEXT

# ==========================================================
# BODY
# ==========================================================

body_style = deepcopy(styles["BodyText"])
body_style.fontName = "Helvetica"
body_style.fontSize = BODY_SIZE
body_style.leading = 12
body_style.alignment = TA_LEFT
body_style.textColor = TEXT

# ==========================================================
# TECHNOLOGY
# ==========================================================

technology_style = deepcopy(styles["BodyText"])
technology_style.fontName = "Helvetica-Bold"
technology_style.fontSize = BODY_SIZE
technology_style.leading = 14
technology_style.alignment = TA_LEFT
technology_style.textColor = SUBTEXT

# ==========================================================
# DATE
# ==========================================================

date_style = deepcopy(styles["BodyText"])
date_style.fontName = "Helvetica-Bold"
date_style.fontSize = BODY_SIZE
date_style.alignment = TA_RIGHT
date_style.textColor = DATE

# ==========================================================
# COLLEGE
# ==========================================================

college_style = deepcopy(styles["BodyText"])
college_style.fontName = "Helvetica"
college_style.fontSize = BODY_SIZE
college_style.leading = 12
college_style.leftIndent = 12
college_style.spaceAfter = 6
college_style.textColor = SUBTEXT