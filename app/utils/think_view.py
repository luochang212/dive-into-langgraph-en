# -*- coding: utf-8 -*-

"""
Optimize thinking process content display
"""

import html


def format_think_result(think_content: str) -> str:
    """
    Format thinking process content and return HTML string.

    :param think_content: Thinking process content
    :return: Formatted HTML string
    """
    if not think_content:
        return ""

    return "\n".join([
        '<details class="think-result-details">',
        '<summary class="think-result-summary">',
        '<div class="think-result-title"> 💭 Thinking</div>',
        '<svg class="think-result-icon" width="20" height="20" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"></polyline></svg>',
        '</summary>',
        '<pre class="think-result-pre">',
        f'\n{html.escape(think_content)}',
        '</pre>',
        '</details>\n\n',
    ])
