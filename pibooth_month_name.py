import pibooth
import datetime

__version__ = "1.0.0"

@pibooth.hookimpl
def pibooth_configure(cfg):
    # Lecture des paramètres configurables dans pibooth.cfg

    # Lecture des mois en chaîne séparée par virgule, exemple: "january,february,march,..."
    months_cfg = cfg.get("PLUGIN_MONTH_NAME", "months", fallback="january,february,march,april,may,june,july,august,september,october,november,december")
    months_list = [m.strip() for m in months_cfg.split(",")]

    # Lecture du format de date
    date_format = cfg.get("PLUGIN_MONTH_NAME", "date_format_footer_text2", fallback="{day} {month} {year}")

    # Date du jour
    today = datetime.date.today()
    day = today.day
    month = months_list[today.month - 1] if 0 <= today.month - 1 < len(months_list) else str(today.month)
    year = today.year

    # Construire la chaîne de date selon le format lu
    date_str = date_format.format(day=day, month=month, year=year)

    # Patcher la configuration pibooth pour la clé footer_text2 dans [PICTURE]
    cfg.set("PICTURE", "footer_text2", date_str)

    print(f"[PLUGIN_MONTH_NAME] footer_text2 set to: {date_str}")
