from reportlab.platypus import (
    Paragraph,
    Spacer,
    HRFlowable,
    Table,
    TableStyle,
    ListFlowable,
    ListItem,
)
from styles import (
    LINE,
    section_style,
    body_style,
    company_style,
    date_style,
    job_style,
)

# =====================================================
# Divider
# =====================================================

def add_divider(story):
    story.append(
        HRFlowable(
            width="100%",
            thickness=0.8,
            color=LINE,
            spaceBefore=3,
            spaceAfter=5,
        )
    )


# =====================================================
# Section Heading
# =====================================================

def add_section_title(story, title):
    story.append(
        Paragraph(
            f"<b>{title}</b>",
            section_style,
        )
    )

    story.append(Spacer(1, 3))


# =====================================================
# Title Row
# =====================================================

def add_title_row(story, title, duration):

    table = Table(
        [[
            Paragraph(title, company_style),
            Paragraph(duration, date_style),
        ]],
        colWidths=["72%", "28%"],
    )

    table.setStyle(
        TableStyle([
            ("ALIGN", (0, 0), (0, 0), "LEFT"),
            ("ALIGN", (1, 0), (1, 0), "RIGHT"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ])
    )

    story.append(table)


# =====================================================
# Job Title
# =====================================================

def add_job_title(story, title):

    story.append(
        Paragraph(
            f"<i>{title}</i>",
            job_style,
        )
    )

    story.append(Spacer(1, 2))


# =====================================================
# Bullet Point
# =====================================================

def add_bullet(story, text):
    story.append(
        Paragraph(
            f"• {text}",
            body_style,
        )
    )

# =====================================================
# Resume Entry
# =====================================================

def add_entry(
    story,
    title,
    subtitle,
    duration,
    bullets,
):
    add_title_row(
        story,
        title,
        duration,
    )

    add_job_title(
        story,
        subtitle,
    )

    for point in bullets:
        add_bullet(
            story,
            point,
        )

    add_divider(story)