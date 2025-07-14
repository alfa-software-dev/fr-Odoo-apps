# -*- coding: utf-8 -*-
{
    'name': "AdlerDo Connector Lite",

    'summary': "Free marketplace reporting & lead generation tool for Odoo",

    'description': """
AdlerDo Connector Lite is a lightweight reporting module designed for visibility, lead generation, and entry-level marketplace transparency.

🎯 Goals:
- Increase visibility in the Odoo App Store
- Provide free, useful features to build trust
- Encourage upgrades to AdlerDo Pro
- Generate leads via built-in demo/contact features
- Promote TecSee GmbH as a trusted Odoo & marketplace integration partner

🔧 Features:
- Read-only marketplace reporting (Amazon, eBay, Kaufland)
- Overview of recent orders
- Daily and monthly revenue dashboard
- Export latest 100 orders to CSV/Excel
- Subtle in-app hint: "For automatic sync, inventory updates, and full multichannel integration, try AdlerDo Pro."
- Direct contact and demo buttons with links to website and calendar
- Footer branding: "Powered by TecSee GmbH – Your digitalization partner for Odoo and marketplaces"
- Automatic email after installation with upgrade/demo offer

🛠 Technical:
- Compatible with Odoo v14–v18, Community & Enterprise
- Lightweight, no sync/write operations
- Dummy data or optional read-only API connection
- Modular structure for easy upgrade to full version
    """,

    'author': "TecSee GmbH",
    'website': "https://www.tecsee.de",

    'category': 'Sales',
    'version': '0.1',

    'depends': ['base'],
    'images' : ['static/description/banner.png'],

    'license': 'Proprietary',
    'application': True,
    'installable': True,
}
