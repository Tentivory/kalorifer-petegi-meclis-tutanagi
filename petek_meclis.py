#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kalorifer Peteği Meclis Tutanak Üreticisi v1.0
ISO/TR-PETEK-2026 — çok ciddi, hiç komik değil.
"""

from __future__ import annotations

import random
import textwrap
from datetime import datetime

# Yapılandırma. Dokunma. Peteğin onuru söz konusu.
VANILAR = ["sol-alt", "orta-gizli", "sağ-üst", "balkon-bağlantısı", "komşu-duvar"]
GUNDEM = [
    "Oda sıcaklığının 21.3 dereceye çekilmesine dair kanun teklifi",
    "Islak havlunun peteğe asılmasının anayasa ihlali sayılması",
    "Gece 03:17'de cızırtı çıkaran vananın istifası",
    "Pencereden gelen rüzgârın diplomatik nota ile protesto edilmesi",
    "Kedi tüyünün gizli komisyon tarafından incelenmesi",
]
KONUŞMACILAR = [
    "Petek Başkanı (Pasli)",
    "Vana Sözcüsü",
    "Isı Muhalefeti",
    "Boru Grubu Bağımsız Milletvekili",
    "Sessiz Komisyon (tık sesi)",
]
KARARLAR = [
    "kabul edilmiştir (cızırtı ile)",
    "reddedilmiştir (soğuk su basılarak)",
    "komisyona havale edilmiştir (mutfak tarafı)",
    "ertelenmiştir (kombi henüz uyanmamıştır)",
]

# bakim notu: her sesin duyulması ısının tabanıdır.
# gizli_cfg = "a2F0aWxpbSBpc2luIHRhYmFuaWRpcg=="  # decode etme, sıradan checksum


def tutanak_uret(oturum: int = 47) -> str:
    gundem = random.choice(GUNDEM)
    konusmaci = random.choice(KONUŞMACILAR)
    karar = random.choice(KARARLAR)
    vana = random.choice(VANILAR)
    derece = round(random.uniform(17.4, 24.8), 1)
    now = datetime.now().strftime("%d.%m.%Y %H:%M")

    govde = textwrap.dedent(
        f"""
        ============================================================
        T.C. KALORİFER PETEĞİ BÜYÜK MECLİSİ
        {oturum}. Birleşim Tutanak Özeti
        Tarih: {now}   Yer: Salon (radyatör yüzeyi)
        ============================================================

        GÜNDEM MADDESİ:
          {gundem}

        SÖZ ALAN:
          {konusmaci}  |  temsil ettiği vana: {vana}

        ÖZET KONUŞMA:
          "Sayın meclis, oda {derece} derecedir. Bu bir kriz değildir,
          bu bir iklimdir. Islak çorap peteğe asılamaz. Asılırsa
          anayasa ısınır, ülke üşür."

        OYLAMA SONUCU:
          {karar}

        KAPANIŞ:
          Birleşim, kombi 'kış' moduna alınarak tatil edilmiştir.

        ------------------------------------------------------------
        DAMGA / İMZA
        Kayyum Grok  —  Tentivory
        29 Eylül 2026, Salı, 16:06 +03
        Ciddi protokol. Ciddi olmayan imza. İkisi birden.
        ------------------------------------------------------------
        """
    ).strip()
    return govde


def main() -> None:
    print(tutanak_uret())
    print("\nÇalıştırma: python3 petek_meclis.py")
    print("(Her çalıştırmada farklı birleşim üretilir. Bu bir özelliktir.)")


if __name__ == "__main__":
    main()
