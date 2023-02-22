# Generated by Django 4.1.7 on 2023-02-21 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("deposits", "0004_alter_deposits_ends_at_alter_deposits_status_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="depositproducts",
            name="valid_currency",
        ),
        migrations.RemoveConstraint(
            model_name="deposits",
            name="valid_status",
        ),
        migrations.AddConstraint(
            model_name="depositproducts",
            constraint=models.CheckConstraint(
                check=models.Q(
                    (
                        "currency__in",
                        [
                            "AFN",
                            "EUR",
                            "ALL",
                            "DZD",
                            "USD",
                            "AOA",
                            "XCD",
                            "ARS",
                            "AMD",
                            "AWG",
                            "AUD",
                            "AZN",
                            "BSD",
                            "BHD",
                            "BDT",
                            "BBD",
                            "BYN",
                            "BZD",
                            "XOF",
                            "BMD",
                            "INR",
                            "BTN",
                            "BOB",
                            "BOV",
                            "BAM",
                            "BWP",
                            "NOK",
                            "BRL",
                            "BND",
                            "BGN",
                            "BIF",
                            "CVE",
                            "KHR",
                            "XAF",
                            "CAD",
                            "KYD",
                            "CLP",
                            "CLF",
                            "CNY",
                            "COP",
                            "COU",
                            "KMF",
                            "CDF",
                            "NZD",
                            "CRC",
                            "HRK",
                            "CUP",
                            "CUC",
                            "ANG",
                            "CZK",
                            "DKK",
                            "DJF",
                            "DOP",
                            "EGP",
                            "SVC",
                            "ERN",
                            "SZL",
                            "ETB",
                            "FKP",
                            "FJD",
                            "XPF",
                            "GMD",
                            "GEL",
                            "GHS",
                            "GIP",
                            "GTQ",
                            "GBP",
                            "GNF",
                            "GYD",
                            "HTG",
                            "HNL",
                            "HKD",
                            "HUF",
                            "ISK",
                            "IDR",
                            "XDR",
                            "IRR",
                            "IQD",
                            "ILS",
                            "JMD",
                            "JPY",
                            "JOD",
                            "KZT",
                            "KES",
                            "KPW",
                            "KRW",
                            "KWD",
                            "KGS",
                            "LAK",
                            "LBP",
                            "LSL",
                            "ZAR",
                            "LRD",
                            "LYD",
                            "CHF",
                            "MOP",
                            "MKD",
                            "MGA",
                            "MWK",
                            "MYR",
                            "MVR",
                            "MRU",
                            "MUR",
                            "XUA",
                            "MXN",
                            "MXV",
                            "MDL",
                            "MNT",
                            "MAD",
                            "MZN",
                            "MMK",
                            "NAD",
                            "NPR",
                            "NIO",
                            "NGN",
                            "OMR",
                            "PKR",
                            "PAB",
                            "PGK",
                            "PYG",
                            "PEN",
                            "PHP",
                            "PLN",
                            "QAR",
                            "RON",
                            "RUB",
                            "RWF",
                            "SHP",
                            "WST",
                            "STN",
                            "SAR",
                            "RSD",
                            "SCR",
                            "SLL",
                            "SLE",
                            "SGD",
                            "XSU",
                            "SBD",
                            "SOS",
                            "SSP",
                            "LKR",
                            "SDG",
                            "SRD",
                            "SEK",
                            "CHE",
                            "CHW",
                            "SYP",
                            "TWD",
                            "TJS",
                            "TZS",
                            "THB",
                            "TOP",
                            "TTD",
                            "TND",
                            "TRY",
                            "TMT",
                            "UGX",
                            "UAH",
                            "AED",
                            "USN",
                            "UYU",
                            "UYI",
                            "UYW",
                            "UZS",
                            "VUV",
                            "VES",
                            "VED",
                            "VND",
                            "YER",
                            "ZMW",
                            "ZWL",
                            "XBA",
                            "XBB",
                            "XBC",
                            "XBD",
                            "XTS",
                            "XXX",
                            "XAU",
                            "XPD",
                            "XPT",
                            "XAG",
                        ],
                    )
                ),
                name="valid_currency_depositProducts",
            ),
        ),
        migrations.AddConstraint(
            model_name="deposits",
            constraint=models.CheckConstraint(
                check=models.Q(("status__in", ["ACTIVE", "CLOSED"])), name="valid_status_deposits"
            ),
        ),
    ]