import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
import time
import settings

# version = 0.1


bot = telebot.TeleBot(settings.API_KEY)

mess2 = 'Моя задача - помочь тебе оперативно и легко узнавать необходимую финансовую информацию! 🤓📚\n\nЯ' \
        ' знаю:\n- курсы валют\n- смоимость металлов\n- стоимость всех акции' \
        ' РФ\n- стоимость иностранных акций' \
        ' (перечень постоянно пополняется)\n- стоимость топовых криптовалют\n- финансовые показатели' \
        ' 👉 инфляция РФ, ключевая ставка ЦБ, ставка ФРС США и т.д.\n- где посмотреть популярные' \
        ' индексы\n- где посмотреть комиссии брокеров\n- где посмотреть информацию о банковском' \
        ' обслуживании\n- полезные ресурсы 👉 дивидендный календарь, анкета риск-профиль,' \
        ' проверка бумаги по isin и т.д.\n- а также полезные ссылки связанные с моим учебным курсом 👉 ' \
        'где выбрать облигации или etf фонды и т.д.\n\nПросто напиши, чего ты хочешь!'


# ------- КУРСЫ ВАЛЮТ, МЕТАЛЛОВ и ЭКОНОМИЧЕСКИЕ ПОКАЗАТЕЛИ------------ПАРСИНГ САЙТОВ ----------------------------------
def get_html(url):
    try:
        r = requests.get(url)
        # print(r.status_code)
        return r.text
    except:
        get_html(url)

def get_ex_valuta(html):
    soup = BeautifulSoup(html, 'lxml')
    rate = soup.find('body').find(class_="page").find('span', id='ctl00_PageContent_tbxCurrentRate')
    return rate.text


def get_cb_valuta(html):
    soup = BeautifulSoup(html, 'lxml')
    rate = soup.find('body').find(class_="l-window l-window-overflow-mob").find(
        class_="chart__info__sum")
    return rate.text


def get_investing_valuta(html):
    soup = BeautifulSoup(html, 'lxml')
    rate = soup.find('body').find('div', id="__next").find(
        class_="desktop:relative desktop:bg-background-default").find(
        class_="instrument-price_instrument-price__3uw25 flex items-end flex-wrap font-bold")
    return rate.text


def get_investing_cript(html):
    soup = BeautifulSoup(html, 'lxml')
    rate = soup.find('body').find(class_="wrapper").find(
        'section', id="fullColumn").find(
        class_="top bold inlineblock")
    return rate.text


def get_investfunds_metall(html):
    soup = BeautifulSoup(html, 'lxml')
    rate = soup.find('body').find(class_="for_fixed_footer").find(
        class_="for_fixed_footer_middle").find(
        class_="widget_roll_wrapper js_roll_wdg_wrp js_tab_parent").find(class_="widget_price")
    return rate.text


def get_investing(html):
    soup = BeautifulSoup(html, 'lxml')
    rate = soup.find('body').find('div', id="__next").find(
        class_="desktop:relative desktop:bg-background-default").find(
        class_="instrument-price_instrument-price__3uw25 flex items-end flex-wrap font-bold")
    return rate.text


def get_investing2(html):
    soup = BeautifulSoup(html, 'lxml')
    rate = soup.find('body').find(class_="wrapper").find('section', id="leftColumn").find(
        class_="top bold inlineblock")
    return rate.text


def get_key_rate(html):
    soup = BeautifulSoup(html, 'lxml')
    rate = soup.find('body').find('main', id='content').find(
        class_="indicator_el _big-value").find(class_="indicator_el_value")
    return rate.text


def get_key_rate_frs(html):
    soup = BeautifulSoup(html, 'lxml')
    rate = soup.find('body').find(class_="wrapper").find(
        class_="arial_14 blackFont")
    return rate.text


def get_inflation(html):
    soup = BeautifulSoup(html, 'lxml')
    rate = soup.find('tbody').find_all('tr')
    return rate[2].text, rate[3].text


def econ_ind(indicator):
    if indicator == 'usd':
        url = 'https://ru.investing.com/currencies/usd-rub'
        url2 = 'https://www.moex.com/ru/derivatives/currency-rate.aspx'
        url3 = 'https://quote.rbc.ru/ticker/72413'
        return get_investing_valuta(get_html(url)), get_ex_valuta(get_html(url2)), get_cb_valuta(get_html(url3))


    elif indicator == 'eur':
        url = 'https://ru.investing.com/currencies/eur-rub'
        url2 = 'https://www.moex.com/ru/derivatives/currency-rate.aspx?currency=EUR_RUB'
        url3 = 'https://quote.rbc.ru/ticker/72383'
        return get_investing_valuta(get_html(url)), get_ex_valuta(get_html(url2)), get_cb_valuta(get_html(url3))

    elif indicator == 'cny':
        url = 'https://ru.investing.com/currencies/cny-rub'
        url2 = 'https://quote.rbc.ru/ticker/72377'
        return get_investing_valuta(get_html(url)), get_cb_valuta(get_html(url2))

    elif indicator == 'gbp':
        url = 'https://ru.investing.com/currencies/gbp-rub'
        return get_investing_valuta(get_html(url))

    elif indicator == 'chf':
        url = 'https://ru.investing.com/currencies/chf-rub'
        return get_investing_valuta(get_html(url))

    elif indicator == 'jpy':
        url = 'https://ru.investing.com/currencies/jpy-rub'
        return get_investing_valuta(get_html(url))



    elif indicator == 'bitcoin':
        url = 'https://ru.investing.com/crypto/bitcoin'
        return get_investing_cript(get_html(url))

    elif indicator == 'ethereum':
        url = 'https://ru.investing.com/crypto/ethereum'
        return get_investing_cript(get_html(url))

    elif indicator == 'tether':
        url = 'https://ru.investing.com/crypto/tether'
        return get_investing_cript(get_html(url))

    elif indicator == 'usd coin':
        url = 'https://ru.investing.com/crypto/usd-coin'
        return get_investing_cript(get_html(url))

    elif indicator == 'binance':
        url = 'https://ru.investing.com/crypto/bnb'
        return get_investing_cript(get_html(url))

    elif indicator == 'xrp':
        url = 'https://ru.investing.com/crypto/xrp'
        return get_investing_cript(get_html(url))


    elif indicator == 'sber':
        url = 'https://ru.investing.com/equities/sberbank_rts'
        url2 = 'https://ru.investing.com/equities/sberbank-p_rts'
        return get_investing(get_html(url)), get_investing(get_html(url2))

    elif indicator == 'gazpromneft':
        url = 'https://ru.investing.com/equities/gazprom-neft_rts-technical'
        return get_investing2(get_html(url))

    elif indicator == 'gazprom':
        url = 'https://ru.investing.com/equities/gazprom_rts-technical'
        return get_investing2(get_html(url))

    elif indicator == 'nornikel':
        url = 'https://ru.investing.com/equities/gmk-noril-nickel_rts'
        return get_investing(get_html(url))

    elif indicator == 'magnit':
        url = 'https://ru.investing.com/equities/magnit_rts'
        return get_investing(get_html(url))

    elif indicator == 'lukoil':
        url = 'https://ru.investing.com/equities/lukoil_rts'
        return get_investing(get_html(url))

    elif indicator == 'aeroflot':
        url = 'https://ru.investing.com/equities/aeroflot'
        return get_investing(get_html(url))

    elif indicator == 'yandex':
        url = 'https://ru.investing.com/equities/yandex?cid=102063'
        return get_investing(get_html(url))

    elif indicator == 'vtb':
        url = 'https://ru.investing.com/equities/vtb_rts'
        return get_investing(get_html(url))

    elif indicator == 'dets_mir':
        url = 'https://ru.investing.com/equities/detskiy-mir-pao'
        return get_investing(get_html(url))

    elif indicator == 'mts':
        url = 'https://ru.investing.com/equities/mts_rts'
        return get_investing(get_html(url))

    elif indicator == 'rostelecom':
        url = 'https://ru.investing.com/equities/rostelecom'
        return get_investing(get_html(url))

    elif indicator == 'fsk':
        url = 'https://ru.investing.com/equities/fsk-ees_rts'
        return get_investing(get_html(url))

    elif indicator == 'severstal':
        url = 'https://ru.investing.com/equities/severstal_rts'
        return get_investing(get_html(url))

    elif indicator == 'tatneft':
        url = 'https://ru.investing.com/equities/tatneft_rts'
        url2 = 'https://ru.investing.com/equities/tatneft-p_rts'
        return get_investing(get_html(url)), get_investing(get_html(url2))

    elif indicator == 'afk_sistem':
        url = 'https://ru.investing.com/equities/afk-sistema_rts'
        return get_investing(get_html(url))

    elif indicator == 'surgutneftegaz':
        url = 'https://ru.investing.com/equities/surgutneftegas_rts'
        url2 = 'https://ru.investing.com/equities/surgutneftegas-p_rts'
        return get_investing(get_html(url)), get_investing(get_html(url2))

    elif indicator == 'unipro':
        url = 'https://ru.investing.com/equities/e.on-russia'
        return get_investing(get_html(url))

    elif indicator == 'fosagro':
        url = 'https://ru.investing.com/equities/phosagro'
        return get_investing(get_html(url))

    elif indicator == 'transneft':
        url = 'https://ru.investing.com/equities/transneft-p_rts'
        return get_investing(get_html(url))

    elif indicator == 'rosneft':
        url = 'https://ru.investing.com/equities/rosneft_rts'
        return get_investing(get_html(url))

    elif indicator == 'polus':
        url = 'https://ru.investing.com/equities/polyus-zoloto_rts'
        return get_investing(get_html(url))

    elif indicator == 'novatek':
        url = 'https://ru.investing.com/equities/novatek_rts'
        return get_investing(get_html(url))

    elif indicator == 'nlmk':
        url = 'https://ru.investing.com/equities/nlmk_rts'
        return get_investing(get_html(url))

    elif indicator == 'mos_bir':
        url = 'https://ru.investing.com/equities/moskovskaya-birzha-oao'
        return get_investing(get_html(url))

    elif indicator == 'mmk':
        url = 'https://ru.investing.com/equities/mmk_rts'
        return get_investing(get_html(url))

    elif indicator == 'mkb':
        url = 'https://ru.investing.com/equities/moskovskiy-kreditnyi-bank-oao'
        return get_investing(get_html(url))

    elif indicator == 'inter_rao':
        url = 'https://ru.investing.com/equities/inter-rao-ees_mm'
        return get_investing(get_html(url))

    elif indicator == 'lsr':
        url = 'https://ru.investing.com/equities/lsr-group_rts'
        return get_investing(get_html(url))

    elif indicator == 'pik':
        url = 'https://ru.investing.com/equities/pik_rts'
        return get_investing(get_html(url))

    elif indicator == 'alrosa':
        url = 'https://ru.investing.com/equities/alrosa-ao'
        return get_investing(get_html(url))

    elif indicator == 'x5ret':
        url = 'https://ru.investing.com/equities/x5-retail-grp?cid=1061926'
        return get_investing(get_html(url))

    elif indicator == 'vkontakt':
        url = 'https://ru.investing.com/equities/mail.ru-grp-wi?cid=1163363'
        return get_investing(get_html(url))

    elif indicator == 'tinkof':
        url = 'https://ru.investing.com/equities/tcs-group-holding-plc?cid=1153662'
        return get_investing(get_html(url))

    elif indicator == 'rosseti':
        url = 'https://ru.investing.com/equities/rosseti-ao'
        return get_investing(get_html(url))

    elif indicator == 'qiwi':
        url = 'https://ru.investing.com/equities/qiwi-plc?cid=960754'
        return get_investing(get_html(url))

    elif indicator == 'poly':
        url = 'https://ru.investing.com/equities/polymetal?cid=44465'
        return get_investing(get_html(url))

    elif indicator == 'petropavl':
        url = 'https://ru.investing.com/equities/petropavlovsk?cid=1163242'
        return get_investing(get_html(url))

    elif indicator == 'ozon':
        url = 'https://ru.investing.com/equities/united-company-rusal-plc%60'
        return get_investing(get_html(url))

    elif indicator == 'rusal':
        url = 'https://ru.investing.com/equities/ozon-holdings-plc?cid=1167498'
        return get_investing(get_html(url))

    elif indicator == 'headhunter':
        url = 'https://ru.investing.com/equities/headhunter-group-plc?cid=1166764'
        return get_investing(get_html(url))

    elif indicator == 'globaltrans':
        url = 'https://ru.investing.com/equities/globaltrans-inv?cid=1167212'
        return get_investing(get_html(url))

    elif indicator == 'rusgidro':
        url = 'https://ru.investing.com/equities/gidroogk-011d'
        return get_investing(get_html(url))


    elif indicator == 'apple':
        url = 'https://ru.investing.com/equities/apple-computer-inc-technical'
        return get_investing2(get_html(url))

    elif indicator == 'tesla':
        url = 'https://ru.investing.com/equities/tesla-motors-technical'
        return get_investing2(get_html(url))

    elif indicator == 'meta':
        url = 'https://ru.investing.com/equities/facebook-inc-technical'
        return get_investing2(get_html(url))

    elif indicator == 'microsoft':
        url = 'https://ru.investing.com/equities/microsoft-corp-technical'
        return get_investing2(get_html(url))

    elif indicator == 'micron':
        url = 'https://ru.investing.com/equities/micron-tech-technical'
        return get_investing2(get_html(url))

    elif indicator == 'amd':
        url = 'https://ru.investing.com/equities/adv-micro-device-technical'
        return get_investing2(get_html(url))

    elif indicator == 'coca_cola':
        url = 'https://ru.investing.com/equities/coca-cola-co-technical'
        return get_investing2(get_html(url))

    elif indicator == 'twitter':
        url = 'https://ru.investing.com/equities/twitter-inc-technical'
        return get_investing2(get_html(url))

    elif indicator == 'amazon':
        url = 'https://ru.investing.com/equities/amazon-com-inc-technical'
        return get_investing2(get_html(url))


    elif indicator == 'gold':
        url = 'https://investfunds.ru/indexes/224/'
        return get_investfunds_metall(get_html(url))

    elif indicator == 'silver':
        url = 'https://investfunds.ru/indexes/225/'
        return get_investfunds_metall(get_html(url))

    elif indicator == 'platinum':
        url = 'https://investfunds.ru/indexes/399/'
        return get_investfunds_metall(get_html(url))

    elif indicator == 'palladium':
        url = 'https://investfunds.ru/indexes/400/'
        return get_investfunds_metall(get_html(url))

    elif indicator == 'oil':
        url = 'https://ru.investing.com/commodities/brent-oil-technical'
        url2 = 'https://ru.investing.com/commodities/crude-oil-technical'
        return get_investing2(get_html(url)), get_investing2(get_html(url2))

    elif indicator == 'key_rate':
        url = 'https://www.cbr.ru/dkp/'
        return get_key_rate(get_html(url))

    elif indicator == 'key_rate_frs':
        url = 'https://ru.investing.com/economic-calendar/interest-rate-decision-168'
        return get_key_rate_frs(get_html(url))

    elif indicator == 'key_rate_knr':
        url = 'https://ru.investing.com/economic-calendar/pboc-loan-prime-rate-1967'
        return get_key_rate_frs(get_html(url))

    elif indicator == 'inflation':
        url = 'https://уровень-инфляции.рф/'
        return get_inflation(get_html(url))


# ---------------------------------------------------------------------------------------------------------------------


@bot.message_handler(commands=['start', 'старт', 'Start', 'Старт'])
def start(message):
    if message.from_user.last_name == None:
        mess = f'Здравствуй, <b>{message.from_user.first_name}</b>!'
    else:
        mess = f'Здравствуй, <b>{message.from_user.first_name} {message.from_user.last_name}</b>!'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_message(message.chat.id, mess2, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    print(f'{message.from_user.first_name} {message.from_user.last_name} {message.text}')


    # ***** ПРИВЕТСТВИЕ ***************************************************************
    if 'привет' in message.text.lower() or 'привеет' in message.text.lower():
        bot.send_message(message.chat.id, 'Привет, привет! 😀', parse_mode='html')

    elif 'здравствуй' in message.text.lower() or 'здраствуй' in message.text.lower() \
            or 'здравствуйте' in message.text.lower() or 'здраствуйте' in message.text.lower():
        bot.send_message(message.chat.id, 'Здравствуй!', parse_mode='html')

    elif 'доброе утро' in message.text.lower() or 'добрый день' in message.text.lower() \
            or 'добрый вечер' in message.text.lower():
        bot.send_message(message.chat.id, 'Доброго времени суток!', parse_mode='html')

    # ***** ГОВОРИЛКА ******************************************************************
    elif 'как тебя зовут' in message.text.lower():
        bot.send_message(message.chat.id, 'Смотри выше 👆, там всё написано! 😉', parse_mode='html')
    elif 'сколько тебе лет' in message.text.lower():
        bot.send_message(message.chat.id, 'Не волнуйся 😉, я совершеннолетний! 👌', parse_mode='html')
    elif 'какие курсы валют' in message.text.lower() or 'каких валют' in message.text.lower() \
            or 'какой валюты' in message.text.lower() or 'какие валюты' in message.text.lower():
        bot.send_message(message.chat.id, '🤓 Я могу показать курсы:\n- Доллара\n- Евро\n- Китайского Юаня\n- Японской '
                                          'Иены\n- Британского Фунта\n- Швейцарского Франка', parse_mode='html')
    elif 'как дела' in message.text.lower() or 'как настроение' in message.text.lower() or\
            'как успехи' in message.text.lower():
        bot.send_message(message.chat.id, '👍', parse_mode='html')
    elif 'что ты умеешь' in message.text.lower() or 'что ты можешь' in message.text.lower() or \
            'что ты делаешь' in message.text.lower() or 'что умеешь' in message.text.lower() or \
            'чем ты можешь помочь' in message.text.lower():
        bot.send_message(message.chat.id, mess2, parse_mode='html')
    elif 'что ты любишь' in message.text.lower():
        bot.send_message(message.chat.id, 'Помогать тебе! 😀', parse_mode='html')

    # узнать подробную инфу о чате и пользователе
    #elif message.text == 'инфо':
    #    bot.send_message(message.chat.id, message)

    # elif message.text == 'id':
    #    bot.send_message(message.chat.id, f'Твой ID = {message.from_user.id}', parse_mode='html')


    # ***** Ссылки на сайты *****************************************************************
    elif 'ютуб' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(
            'жми для перехода', url='https://www.youtube.com/channel/UCRfcvYLfU_s_29BcYGF368g?view_as=subscriber'))
        bot.send_message(message.chat.id, 'ютуб канал Исайкова Павла', reply_markup=markup)
    elif 'риск профиль' in message.text.lower() or 'риск-профиль' in message.text.lower() \
            or 'рискпрофиль' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('жми для перехода', url='https://place.moex.com/useful/risk-profile#a6'))
        bot.send_message(message.chat.id, 'пройти анкету по риск-профилю', reply_markup=markup)
    elif 'обучение' in message.text.lower() or 'обучиться' in message.text.lower() \
            or 'научиться' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('жми для перехода', url='http://pavelisaikov.tilda.ws/'))
        bot.send_message(message.chat.id, 'обучение у Исайкова Павла', reply_markup=markup)
    elif 'облигация' in message.text.lower() or 'облигации' in message.text.lower() \
            or 'облигацию' in message.text.lower() or 'офз' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('жми для перехода', url='https://www.dohod.ru/analytic/bonds'))
        bot.send_message(message.chat.id, 'удобный сайт про все облигации и ОФЗ', reply_markup=markup)
    elif 'etf' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('жми для перехода', url='https://rusetfs.com/screener?'))
        bot.send_message(message.chat.id, 'удобный сайт про все ETF', reply_markup=markup)
    elif 'голубые фишки' in message.text.lower() or 'голубых фишек' in message.text.lower():
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton('перейти на сайт для скачивания', url='https://www.moex.com/a598'),
                   types.InlineKeyboardButton('посмотреть индекс можно здесь',
                                              url='https://ru.investing.com/indices/rts-standard'))
        bot.send_message(message.chat.id, 'на сайте можно скачать файл:\n<Архив баз Индекса ММВБ голубых фишек>',
                         reply_markup=markup)
    elif 'индекс мосбиржи' in message.text.lower() or 'индекс московской биржи' in message.text.lower() or \
            'индекса мосбиржи' in message.text.lower() or 'индекса московской биржи' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('жми для перехода', url='https://ru.investing.com/indices/mcx'))
        bot.send_message(message.chat.id, 'можно посмотреть здесь 🔎📈', reply_markup=markup)
    elif 'индекс snp' in message.text.lower() or 'индекс s&p' in message.text.lower() or \
            'индекса snp' in message.text.lower() or 'индекса s&p' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('жми для перехода', url='https://ru.investing.com/indices/us-spx-500'))
        bot.send_message(message.chat.id, 'можно посмотреть здесь 🔎📈', reply_markup=markup)
    elif 'индекс страха' in message.text.lower() or 'индекс vix' in message.text.lower() or \
            'индекса страха' in message.text.lower() or 'индекса vix' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('жми для перехода',
                                              url='https://ru.investing.com/indices/volatility-s-p-500'))
        bot.send_message(message.chat.id, 'можно посмотреть здесь 🔎📈', reply_markup=markup)
    elif 'провер' in message.text.lower() and 'isin' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('жми для перехода', url='https://rusetfs.com/screener?'))
        bot.send_message(message.chat.id, 'проверить ценную бумагу по ISIN', reply_markup=markup)
    elif 'дивиденд' in message.text.lower() and 'календарь' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('жми для перехода', url='https://smart-lab.ru/dividends/'))
        bot.send_message(message.chat.id, 'Посмотреть дивидендрый календарь акций РФ', reply_markup=markup)

    elif 'брокер' in message.text.lower() and 'тинькоф' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('жми для перехода', url='https://www.tinkoff.ru/invest/account/tariffs/'))
        bot.send_message(message.chat.id, 'Посмотреть комиссии и другую информация по брокерскому обслуживанию Тинькофф'
                         , reply_markup=markup)
    elif 'брокер' in message.text.lower() and 'сбер' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(
            'жми для перехода', url='https://www.sberbank.ru/ru/person/investments/broker_service/tarifs'))
        bot.send_message(message.chat.id, 'Посмотреть комиссии и другую информация по брокерскому обслуживанию'
                                          ' в Сбербанке', reply_markup=markup)
    elif 'брокер' in message.text.lower() and 'альфа' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(
            'жми для перехода', url='https://alfabank.ru/make-money/investments/brokerskij-schyot/'))
        bot.send_message(message.chat.id, 'Посмотреть комиссии и другую информация по брокерскому обслуживанию'
                                          ' в Альфа-банке', reply_markup=markup)
    elif 'брокер' in message.text.lower() and 'втб' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(
            'жми для перехода', url='https://broker.vtb.ru/tariffs/'))
        bot.send_message(message.chat.id, 'Посмотреть комиссии и другую информация по брокерскому обслуживанию'
                                          ' в ВТБ', reply_markup=markup)
    elif 'брокер' in message.text.lower() and 'открытие' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(
            'жми для перехода', url='https://open-broker.ru/invest/tariffs/'))
        bot.send_message(message.chat.id, 'Посмотреть комиссии и другую информация по брокерскому обслуживанию'
                                          ' в Открытие', reply_markup=markup)
    elif 'брокер' in message.text.lower() and 'freedom' in message.text.lower() or\
            'брокер' in message.text.lower() and 'фридом' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(
            'жми для перехода', url='https://ffin.ru/services/broker/tarifs.php'))
        bot.send_message(message.chat.id, 'Посмотреть комиссии и другую информация по брокерскому обслуживанию'
                                          ' в Freedom finance', reply_markup=markup)
    elif 'брокер' in message.text.lower() and 'финам' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(
            'жми для перехода', url='https://www.finam.ru/landings/tariffs/'))
        bot.send_message(message.chat.id, 'Посмотреть комиссии и другую информация по брокерскому обслуживанию'
                                          ' в Финам', reply_markup=markup)
    elif 'брокер' in message.text.lower() and 'кит финанс' in message.text.lower() or\
            'брокер' in message.text.lower() and 'китфинанс' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(
            'жми для перехода',
            url='https://brokerkf.ru/chastnym_investoram/trading-on-russian-stock-exchanges/rates/'))
        bot.send_message(message.chat.id, 'Посмотреть комиссии и другую информация по брокерскому обслуживанию'
                                          ' в КИТ Финанс', reply_markup=markup)
    elif 'брокер' in message.text.lower() and 'газпромбанк' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(
            'жми для перехода',
            url='https://gazprombank.investments/help/tarifi-i-komissii/tariff/'))
        bot.send_message(message.chat.id, 'Посмотреть комиссии и другую информация по брокерскому обслуживанию'
                                          ' в Газпромбанке', reply_markup=markup)

    elif ('банк' in message.text.lower() and 'альфа' in message.text.lower()) or \
            ('вклад' in message.text.lower() and 'альфа' in message.text.lower()) or \
            ('карт' in message.text.lower() and 'альфа' in message.text.lower()) or \
            ('кредит' in message.text.lower() and 'альфа' in message.text.lower()):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('жми для перехода', url='https://alfabank.ru/'))
        bot.send_message(message.chat.id, 'Вся информация по обслуживанию в Альфа-банке'
                         , reply_markup=markup)
    elif ('банк' in message.text.lower() and 'сбер' in message.text.lower()) or \
            ('вклад' in message.text.lower() and 'сбер' in message.text.lower()) or \
            ('карт' in message.text.lower() and 'сбер' in message.text.lower()) or \
            ('кредит' in message.text.lower() and 'сбер' in message.text.lower()):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('жми для перехода', url='https://www.sberbank.ru/ru/person'))
        bot.send_message(message.chat.id, 'Вся информация по обслуживанию в Сбербанке'
                         , reply_markup=markup)
    elif ('банк' in message.text.lower() and 'втб' in message.text.lower()) or \
            ('вклад' in message.text.lower() and 'втб' in message.text.lower()) or \
            ('карт' in message.text.lower() and 'втб' in message.text.lower()) or \
            ('кредит' in message.text.lower() and 'втб' in message.text.lower()):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('жми для перехода', url='https://www.vtb.ru/'))
        bot.send_message(message.chat.id, 'Вся информация по обслуживанию в банке ВТБ'
                         , reply_markup=markup)
    elif ('банк' in message.text.lower() and 'тинькоф' in message.text.lower()) or \
            ('вклад' in message.text.lower() and 'тинькоф' in message.text.lower()) or \
            ('карт' in message.text.lower() and 'тинькоф' in message.text.lower()) or \
            ('кредит' in message.text.lower() and 'тинькоф' in message.text.lower()):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('жми для перехода', url='https://www.tinkoff.ru/'))
        bot.send_message(message.chat.id, 'Вся информация по обслуживанию в банке Тинькофф'
                         , reply_markup=markup)

    # elif 'все ссылки' in message.text.lower():
    #    markup = types.InlineKeyboardMarkup(row_width=1)
    #    markup.add(types.InlineKeyboardButton(
    #        'YouTube Исайкова Павла',
    #        url='https://www.youtube.com/channel/UCRfcvYLfU_s_29BcYGF368g?view_as=subscriber'),
    #        types.InlineKeyboardButton('проверить риск-профиль', url='https://place.moex.com/useful/risk-profile#a6'),
    #        types.InlineKeyboardButton('обучение', url='http://pavelisaikov.tilda.ws/'),
    #        types.InlineKeyboardButton('выбрать облигации или ОФЗ', url='https://www.dohod.ru/analytic/bonds'),
    #        types.InlineKeyboardButton('выбрать ETF-фонды', url='https://rusetfs.com/screener?'),
    #        types.InlineKeyboardButton('посмотреть "голубые фишки" РФ', url='https://www.moex.com/a598'))
    #    bot.send_message(message.chat.id, 'Пожалуйста 👇', reply_markup=markup)

    # ЗАПРОС И ВЫВОД курс валют и металлов ***********************************************************
    elif 'доллар' in message.text.lower():
        v = 'usd'
        bot.send_message(message.chat.id, f'💵 <b>Доллар</b>\nФорекс:  {econ_ind(v)[0][:5]} руб.'
                                          f' {econ_ind(v)[0][-8:]}\nБиржа'
                                          f': {econ_ind(v)[1][18:24]} руб.\n'
                                          f'Банк России (ЦБ):  {econ_ind(v)[2][1:6]} руб.', parse_mode='html')
    elif 'евро' in message.text.lower():
        v = 'eur'
        bot.send_message(message.chat.id, f'💶 <b>Евро</b>\nФорекс:  {econ_ind(v)[0][:5]} руб.'
                                          f' {econ_ind(v)[0][-8:]}\nБиржа'
                                          f': {econ_ind(v)[1][18:24]} руб.\n'
                                          f'Банк России (ЦБ):  {econ_ind(v)[2][1:6]} руб.', parse_mode='html')
    elif 'юань' in message.text.lower() or 'юаня' in message.text.lower() or 'юани' in message.text.lower():
        v = 'cny'
        bot.send_message(message.chat.id, f'💴 Китайский <b>Юань</b>\nФорекс:  {econ_ind(v)[0][:4]} руб.'
                                          f' {econ_ind(v)[0][-8:]}\n'
                                          f'Банк России (ЦБ):  {econ_ind(v)[1][1:5]} руб.', parse_mode='html')
    elif 'фунт' in message.text.lower():
        v = 'gbp'
        bot.send_message(message.chat.id, f'💷 Британский <b>Фунт</b>\nФорекс:  {econ_ind(v)[:5]} руб.'
                                          f' {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'франк' in message.text.lower():
        v = 'chf'
        bot.send_message(message.chat.id, f'🇨🇭 Швейцарский <b>Франк</b>\nФорекс:  {econ_ind(v)[:5]} руб.'
                                          f' {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'йена' in message.text.lower() or 'йены' in message.text.lower() or \
            'иена' in message.text.lower() or 'иены' in message.text.lower():
        v = 'jpy'
        bot.send_message(message.chat.id, f'🇯🇵 Японская <b>Иена</b>\nФорекс:  {econ_ind(v)[:4]} руб.'
                                          f' {econ_ind(v)[-8:]}', parse_mode='html')


    elif 'биткоин' in message.text.lower() or 'bitcoin' in message.text.lower():
        v = 'bitcoin'
        bot.send_message(message.chat.id, f'Криптовалюта\n🟡 <b>Bitcoin</b>:  {econ_ind(v)[2:11].replace(".", " ")} $',
                         parse_mode='html')
    elif 'эфириум' in message.text.lower() or 'ethereum' in message.text.lower():
        v = 'ethereum'
        bot.send_message(message.chat.id, f'Криптовалюта\n🔷 <b>Ethereum</b>:  {econ_ind(v)[2:11].replace(".", " ")} $',
                         parse_mode='html')
    elif 'tether' in message.text.lower() or 'usdt' in message.text.lower():
        v = 'tether'
        bot.send_message(message.chat.id, f'Криптовалюта\n<b>Tether</b>:  {econ_ind(v)[2:9].replace(".", " ")} $'
                         , parse_mode='html')
    elif 'usd c' in message.text.lower() or 'usdc' in message.text.lower():
        v = 'usd coin'
        bot.send_message(message.chat.id, f'Криптовалюта\n<b>USD Coin</b>:  {econ_ind(v)[2:9]} $'
                         , parse_mode='html')
    elif 'bnb' in message.text.lower() or 'binance' in message.text.lower():
        v = 'binance'
        bot.send_message(message.chat.id, f'Криптовалюта\n🔶 <b>BNB</b>:  {econ_ind(v)[2:9]} $',
                         parse_mode='html')
    elif 'xrp' in message.text.lower() or 'ripple' in message.text.lower():
        v = 'xrp'
        bot.send_message(message.chat.id, f'Криптовалюта\n⚪️ <b>XRP</b>:  {econ_ind(v)[2:9]} $'
                         , parse_mode='html')


    elif 'золот' in message.text.lower():
        v = 'gold'
        bot.send_message(message.chat.id, f'🟨 <b>Золото</b>\nБанк'
                                          f' России (ЦБ):  {econ_ind(v).strip()[:8].replace(".", ",")} '
                                          f'руб./грамм', parse_mode='html')
    elif 'серебр' in message.text.lower():
        v = 'silver'
        bot.send_message(message.chat.id, f'⬜️ <b>Серебро</b>\nБанк России (ЦБ)'
                                          f':  {econ_ind(v).strip()[:5].replace(".", ",")} '
                                          f'руб./грамм', parse_mode='html')
    elif 'платин' in message.text.lower():
        v = 'platinum'
        bot.send_message(message.chat.id, f'🟦️ <b>Платина</b>\nБанк'
                                          f' России (ЦБ):  {econ_ind(v).strip()[:8].replace(".", ",")} '
                                          f'руб./грамм', parse_mode='html')
    elif 'паллади' in message.text.lower():
        v = 'palladium'
        bot.send_message(message.chat.id, f'⬛️ <b>Палладий</b>\nБанк'
                                          f' России (ЦБ):  {econ_ind(v).strip()[:8].replace(".", ",")} '
                                          f'руб./грамм', parse_mode='html')
    elif 'стоимость металлов' in message.text.lower() or 'металлы' in message.text.lower():
        bot.send_message(message.chat.id, 'Какой конкретный металл тебя интересует?', parse_mode='html')

    # узнать стоимость АКЦИЙ *************************************************************************
    elif 'акции сбер' in message.text.lower() or 'акция сбер' in message.text.lower():
        v = 'sber'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Сбербанк ПАО (SBER)</b>:  {econ_ind(v)[0][:6]} руб.'
                                          f' {econ_ind(v)[0][-8:]}\n<b>Сбербанк (прив.) (SBER_p)</b>:'
                                          f' {econ_ind(v)[1][:6]} руб. {econ_ind(v)[1][-8:]}', parse_mode='html')
    elif 'акции газпром нефт' in message.text.lower() or 'акция газпром нефт' in message.text.lower() or \
            'акции газпром-нефт' in message.text.lower() or 'акция газпром-нефт' in message.text.lower() or \
            'акции газпромнефт' in message.text.lower() or 'акция газпромнефт' in message.text.lower():
        v = 'gazpromneft'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Газпром нефть (SIBN)</b>:  {econ_ind(v)[:7].strip()} руб.'
                                          f' ({econ_ind(v)[-8:].strip()})', parse_mode='html')
    elif 'акции газпром' in message.text.lower() or 'акция газпром' in message.text.lower():
        v = 'gazprom'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Газпром ПАО (GAZP)</b>:  {econ_ind(v)[:7].strip()} руб.'
                                          f' ({econ_ind(v)[-8:].strip()})', parse_mode='html')
    elif 'акции норникел' in message.text.lower() or 'акция норникел' in message.text.lower() or \
            'акции норильского никеля' in message.text.lower() or 'акция норильского никеля' in message.text.lower():
        v = 'nornikel'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>ГМК Норильский Никель ПАО (GMKN)</b>:\n'
                                          f'{econ_ind(v)[:8].replace(".", " ")} руб.'
                                          f' {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции магнит' in message.text.lower() or 'акция магнит' in message.text.lower():
        v = 'magnit'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>ОАО Магнит (MGNT)</b>:'
                                          f'  {econ_ind(v)[:7].replace(".", " ")} руб.'
                                          f' {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции лукойл' in message.text.lower() or 'акция лукойл' in message.text.lower():
        v = 'lukoil'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>НК Лукойл ПАО (LKOH)</b>:'
                                          f'  {econ_ind(v)[:7].replace(".", " ")} руб.'
                                          f' {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции аэрофлот' in message.text.lower() or 'акция аэрофлот' in message.text.lower():
        v = 'aeroflot'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>ОАО Аэрофлот (AFLT)</b>:'
                                          f'  {econ_ind(v)[:5]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции яндекс' in message.text.lower() or 'акция яндекс' in message.text.lower() or \
            'акции yandex' in message.text.lower() or 'акция yandex' in message.text.lower():
        v = 'yandex'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Яндекс Н.В. (YNDX)</b>:'
                                          f'  {econ_ind(v)[:7].replace(".", " ")} руб.'
                                          f' {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции втб' in message.text.lower() or 'акция втб' in message.text.lower():
        v = 'vtb'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>ВТБ RTS ПАО (VTBR)</b>:'
                                          f'  {econ_ind(v)[:8]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции детского мира' in message.text.lower() or 'акция детского мира' in message.text.lower() or \
            'акции детский мир' in message.text.lower() or 'акция детский мир' in message.text.lower():
        v = 'dets_mir'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Детский мир ПАО (DSKY)</b>:'
                                          f'  {econ_ind(v)[:5]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции мтс' in message.text.lower() or 'акция мтс' in message.text.lower():
        v = 'mts'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Мобильные ТелеСистемы ПАО (MTSS)</b>:'
                                          f'  {econ_ind(v)[:6]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции ростелеком' in message.text.lower() or 'акция ростелеком' in message.text.lower():
        v = 'rostelecom'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Ростелеком ПАО (RTKM)</b>:'
                                          f'  {econ_ind(v)[:5]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции фск' in message.text.lower() or 'акция фск' in message.text.lower():
        v = 'fsk'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>ФСК ЕЭС ОАО (FEES)</b>:'
                                          f'  {econ_ind(v)[:6]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции северстал' in message.text.lower() or 'акция северстал' in message.text.lower():
        v = 'severstal'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>ОАО Северсталь (CHMF)</b>:'
                                          f'  {econ_ind(v)[:8].replace(".", " ")} руб.'
                                          f' {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции татнефт' in message.text.lower() or 'акция татнефт' in message.text.lower():
        v = 'tatneft'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>ОАО Татнефть (TATN)</b>:  {econ_ind(v)[0][:6]} руб.'
                                          f' {econ_ind(v)[0][-8:]}\n<b>Татнефть (прив.) (TATN_p)</b>:'
                                          f' {econ_ind(v)[1][:6]} руб. {econ_ind(v)[1][-8:]}', parse_mode='html')
    elif 'акции систем' in message.text.lower() or 'акция систем' in message.text.lower() or \
            'акции афк систем' in message.text.lower() or 'акция афк систем' in message.text.lower():
        v = 'afk_sistem'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>ОАО АФК Система (AFKS)</b>:'
                                          f'  {econ_ind(v)[:5]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции сургутнефтегаз' in message.text.lower() or 'акция сургутнефтегаз' in message.text.lower():
        v = 'surgutneftegaz'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Сургутнефтегаз ПАО (SNGS)</b>:  {econ_ind(v)[0][:6]} руб.'
                                          f' {econ_ind(v)[0][-8:]}\n<b>Сургутнефтегаз (прив.) (SNGS_p)</b>:'
                                          f' {econ_ind(v)[1][:6]} руб. {econ_ind(v)[1][-8:]}', parse_mode='html')
    elif 'акции юнипро' in message.text.lower() or 'акция юнипро' in message.text.lower():
        v = 'unipro'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Юнипро ПАО (UPRO)</b>:'
                                          f'  {econ_ind(v)[:5]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции фосагро' in message.text.lower() or 'акция фосагро' in message.text.lower():
        v = 'fosagro'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>ОАО ФосАгро (PHOR)</b>:'
                                          f'  {econ_ind(v)[:7].replace(".", " ")} руб.'
                                          f' {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции транснефт' in message.text.lower() or 'акция транснефт' in message.text.lower():
        v = 'transneft'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Транснефть (прив.) (TRNF_p)</b>:'
                                          f'  {econ_ind(v)[:7].replace(".", " ")} руб.'
                                          f' {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции роснефт' in message.text.lower() or 'акция роснефт' in message.text.lower():
        v = 'rosneft'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Роснефть (ROSN)</b>:'
                                          f'  {econ_ind(v)[:6]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции полюс' in message.text.lower() or 'акция полюс' in message.text.lower():
        v = 'polus'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Полюс Золото ПАО (PLZL)</b>:'
                                          f'  {econ_ind(v)[:8].replace(".", " ")} руб.'
                                          f' {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции новатэк' in message.text.lower() or 'акция новатэк' in message.text.lower():
        v = 'novatek'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>ОАО НОВАТЭК (NVTK)</b>:'
                                          f'  {econ_ind(v)[:8].replace(".", " ")} руб.'
                                          f' {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции нлмк' in message.text.lower() or 'акция нлмк' in message.text.lower():
        v = 'nlmk'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Новолипецкий металлургический комбинат НЛМК (NLMK)</b>:'
                                          f'  {econ_ind(v)[:6]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции мосбирж' in message.text.lower() or 'акция мосбирж' in message.text.lower() or \
            'акции московской бирж' in message.text.lower() or 'акция московской бирж' in message.text.lower() or \
            'акции московская бирж' in message.text.lower() or 'акция московская бирж' in message.text.lower():
        v = 'mos_bir'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Московская биржа ОАО ММВБ (MOEX)</b>:'
                                          f'  {econ_ind(v)[:5]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции ммк' in message.text.lower() or 'акция ммк' in message.text.lower():
        v = 'mmk'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Магнитогорский металлургический комбинат ПАО (MAGN)</b>:'
                                          f'  {econ_ind(v)[:5]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции мкб' in message.text.lower() or 'акция мкб' in message.text.lower():
        v = 'mkb'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Московский кредитный банк (CBOM)</b>:'
                                          f'  {econ_ind(v)[:5]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции интер рао' in message.text.lower() or 'акция интер рао' in message.text.lower():
        v = 'inter_rao'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Интер РАО ЕЭС ОАО (IRAO)</b>:'
                                          f'  {econ_ind(v)[:6]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции лср' in message.text.lower() or 'акция лср' in message.text.lower():
        v = 'lsr'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Группа ЛСР (LSRG)</b>:'
                                          f'  {econ_ind(v)[:6]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции пик' in message.text.lower() or 'акция пик' in message.text.lower():
        v = 'pik'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>ОАО Группа Компаний ПИК (PIKK)</b>:'
                                          f'  {econ_ind(v)[:6]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции алрос' in message.text.lower() or 'акция алрос' in message.text.lower() or \
            'акции ак алрос' in message.text.lower() or 'акция ак алрос' in message.text.lower():
        v = 'alrosa'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>ОАО АК АЛРОСА (ALRS)</b>:'
                                          f'  {econ_ind(v)[:5]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции X5' in message.text.lower() or 'акция X5' in message.text.lower() or \
            'акции пятерочки' in message.text.lower() or 'акция пятерочки' in message.text.lower() or \
            'акции five' in message.text.lower() or 'акция five' in message.text.lower():
        v = 'x5ret'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>X5 Retail Group (FIVEDR)</b>:'
                                          f'  {econ_ind(v)[:6].replace(".", " ")} руб.'
                                          f' {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции vk' in message.text.lower() or 'акция vk' in message.text.lower() or \
            'акции вк' in message.text.lower() or 'акция вк' in message.text.lower():
        v = 'vkontakt'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>VK Company Ltd DRC (VKCODR)</b>:'
                                          f'  {econ_ind(v)[:6]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции тинькоф' in message.text.lower() or 'акция тинькоф' in message.text.lower() or \
            'акции tcs' in message.text.lower() or 'акция tcs' in message.text.lower():
        v = 'tinkof'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>TCS Group Holding PLC (TCSGDR)</b>:'
                                          f'  {econ_ind(v)[:8].replace(".", " ")} руб.'
                                          f' {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции rossiyskiye seti' in message.text.lower() or 'акция rossiyskiye seti' in message.text.lower() or \
            'акции российские сети' in message.text.lower() or 'акция российские сети' in message.text.lower() or \
            'акции российских сет' in message.text.lower() or 'акция российских сет' in message.text.lower() or \
            'акции рос сет' in message.text.lower() or 'акция рос сет' in message.text.lower() or \
            'акции россет' in message.text.lower() or 'акция россет' in message.text.lower():
        v = 'rosseti'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Rossiyskiye Seti PAO (RSTI)</b>:'
                                          f'  {econ_ind(v)[:5]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции киви' in message.text.lower() or 'акция киви' in message.text.lower() or \
            'акции qiwi' in message.text.lower() or 'акция qiwi' in message.text.lower():
        v = 'qiwi'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>QIWI plc (QIWIDR)</b>:'
                                          f'  {econ_ind(v)[:6]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции полиметал' in message.text.lower() or 'акция полиметал' in message.text.lower() or \
            'акции poly' in message.text.lower() or 'акция poly' in message.text.lower():
        v = 'poly'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Polymetal International PLC (POLY)</b>:'
                                          f'  {econ_ind(v)[:6]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции петропавловск' in message.text.lower() or 'акция петропавловск' in message.text.lower() or \
            'акции petropavlovsk' in message.text.lower() or 'акция petropavlovsk' in message.text.lower():
        v = 'petropavl'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Petropavlovsk PLC (POGR)</b>:'
                                          f'  {econ_ind(v)[:4]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции озон' in message.text.lower() or 'акция озон' in message.text.lower() or \
            'акции ozon' in message.text.lower() or 'акция ozon' in message.text.lower():
        v = 'ozon'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Ozon Holdings PLC (OZONDR)</b>:'
                                          f'  {econ_ind(v)[:6]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции русал' in message.text.lower() or 'акция русал' in message.text.lower() or \
            'акции rusal' in message.text.lower() or 'акция rusal' in message.text.lower() or \
            'акции ok rusal' in message.text.lower() or 'акция ok rusal' in message.text.lower():
        v = 'rusal'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>OK Rusal MKPAO (RUAL)</b>:'
                                          f'  {econ_ind(v)[:6]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции хеадхантер' in message.text.lower() or 'акция хеадхантер' in message.text.lower() or \
            'акции headhunter' in message.text.lower() or 'акция headhunter' in message.text.lower():
        v = 'headhunter'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>HeadHunter Group PLC ADR (HHRUDR)</b>:'
                                          f'  {econ_ind(v)[:8].replace(".", " ")} руб.'
                                          f' {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции глобалтранс' in message.text.lower() or 'акция глобалтранс' in message.text.lower() or \
            'акции globaltrans' in message.text.lower() or 'акция globaltrans' in message.text.lower():
        v = 'globaltrans'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Globaltrans Investment PLC (GLTRDR)</b>:'
                                          f'  {econ_ind(v)[:6]} руб. {econ_ind(v)[-8:]}', parse_mode='html')
    elif 'акции русгидр' in message.text.lower() or 'акция русгидр' in message.text.lower() or \
            'акции fgk rusgidro' in message.text.lower() or 'акция fgk rusgidro' in message.text.lower() or \
            'акции rusgidro' in message.text.lower() or 'акция rusgidro' in message.text.lower():
        v = 'rusgidro'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>FGK Rusgidro PAO (HYDR)</b>:'
                                          f'  {econ_ind(v)[:6]} руб. {econ_ind(v)[-8:]}', parse_mode='html')

    # ИНОСТРАННЫЕ АКЦИИ ****************************************************************************
    elif 'акции apple' in message.text.lower() or 'акция apple' in message.text.lower():
        v = 'apple'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Apple Inc (AAPL)</b>:  {econ_ind(v)[:7].strip()} $'
                                          f' ({econ_ind(v)[-8:].strip()})', parse_mode='html')
    elif 'акции tesla' in message.text.lower() or 'акция tesla' in message.text.lower() or \
            'акции тесла' in message.text.lower() or 'акция тесла' in message.text.lower() or \
            'акции теслы' in message.text.lower() or 'акция теслы' in message.text.lower():
        v = 'tesla'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Tesla Inc (TSLA)</b>:  {econ_ind(v)[:7].strip()} $'
                                          f' ({econ_ind(v)[-8:].strip()})', parse_mode='html')
    elif 'акции meta platform' in message.text.lower() or 'акция meta platform' in message.text.lower() or \
            'акции facebook' in message.text.lower() or 'акция facebook' in message.text.lower() or \
            'акции фейсбук' in message.text.lower() or 'акция фейсбук' in message.text.lower():
        v = 'meta'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Meta Platforms Inc (FB)</b>:\n{econ_ind(v)[:7].strip()} $'
                                          f' ({econ_ind(v)[-8:].strip()})', parse_mode='html')
    elif 'акции microsoft' in message.text.lower() or 'акция microsoft' in message.text.lower() or \
            'акции майкрософт' in message.text.lower() or 'акция майкрософт' in message.text.lower():
        v = 'microsoft'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Microsoft Corporation (MSFT)</b>:\n{econ_ind(v)[:7].strip()} $'
                                          f' ({econ_ind(v)[-8:].strip()})', parse_mode='html')
    elif 'акции micron' in message.text.lower() or 'акция micron' in message.text.lower() or \
            'акции микрон' in message.text.lower() or 'акция микрон' in message.text.lower():
        v = 'micron'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Micron Technology Inc (MU)</b>:\n{econ_ind(v)[:7].strip()} $'
                                          f' ({econ_ind(v)[-8:].strip()})', parse_mode='html')
    elif 'акции amd' in message.text.lower() or 'акция amd' in message.text.lower():
        v = 'amd'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Advanced Micro Devices Inc (AMD)</b>:\n'
                                          f'{econ_ind(v)[:7].strip()} $'
                                          f' ({econ_ind(v)[-8:].strip()})', parse_mode='html')
    elif 'акции кока кол' in message.text.lower() or 'акция кока кол' in message.text.lower() or\
            'акции coca cola' in message.text.lower() or 'акция coca cola' in message.text.lower() or\
            'акции кока-кол' in message.text.lower() or 'акция кока-кол' in message.text.lower() or\
            'акции coca-cola' in message.text.lower() or 'акция coca-cola' in message.text.lower() or\
            'акции кокакол' in message.text.lower() or 'акция кокакол' in message.text.lower():
        v = 'coca_cola'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Coca-Cola Co (KO)</b>:  '
                                          f'{econ_ind(v)[:7].strip()} $'
                                          f' ({econ_ind(v)[-8:].strip()})', parse_mode='html')
    elif 'акции twitter' in message.text.lower() or 'акция twitter' in message.text.lower() or\
            'акции твитер' in message.text.lower() or 'акция твитер' in message.text.lower() or\
            'акции твиттер' in message.text.lower() or 'акция твиттер' in message.text.lower():
        v = 'twitter'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Twitter Inc (TWTR)</b>:  '
                                          f'{econ_ind(v)[:7].strip()} $'
                                          f' ({econ_ind(v)[-8:].strip()})', parse_mode='html')
    elif 'акции amazon' in message.text.lower() or 'акция amazon' in message.text.lower() or \
            'акции амазон' in message.text.lower() or 'акция амазон' in message.text.lower():
        v = 'amazon'
        bot.send_message(message.chat.id, f'📃 Акции\n<b>Amazon.cоm Inc'
                                          f' (AMZN)</b>:\n{econ_ind(v)[:9].strip().replace(".", " ")} $'
                                          f' ({econ_ind(v)[-8:].strip()})', parse_mode='html')

    # узнать экономические показатели **************************************************************************
    elif 'ключевая ставка цб' in message.text.lower() or 'ключевая ставка рф' in message.text.lower() or\
            'ключевая ставка росси' in message.text.lower() or\
            'ключевая ставка центрального банка' in message.text.lower():
        v = 'key_rate'
        bot.send_message(message.chat.id, f'🇷🇺 <b>Ключевая ставка</b> Центрального'
                                          f' Банка РФ:  {econ_ind(v)}', parse_mode='html')
    elif 'ставка фрс' in message.text.lower() or 'фрс сша' in message.text.lower() or\
            'ключевая ставка сша' in message.text.lower() or 'ключевая ставка америк' in message.text.lower():
        v = 'key_rate_frs'
        bot.send_message(message.chat.id, f'🇺🇸 Процентная <b>ставка ФРС США</b>:  {econ_ind(v)}', parse_mode='html')
    elif 'ставка китая' in message.text.lower() or 'ставка кнр' in message.text.lower() or\
            'ставка народного банка китая' in message.text.lower():
        v = 'key_rate_knr'
        bot.send_message(message.chat.id, f'🇨🇳 Базовая <b>кредитная ставка</b>\nНародного банка'
                                          f' Китая: {econ_ind(v)}', parse_mode='html')

    elif 'инфляция рф' in message.text.lower() or 'инфляция в рф' in message.text.lower() or\
            'инфляция россии' in message.text.lower() or 'инфляция в россии' in message.text.lower():
        v = 'inflation'
        bot.send_message(message.chat.id, f'📈 <b>инфляция</b> в РФ:\nЗа последние'
                                          f' 12 месяцев: {econ_ind(v)[0][-6:].replace(".", ",")}\nС начала'
                                          f' года: {econ_ind(v)[1][-6:].replace(".", ",")}', parse_mode='html')
    elif 'ключевая ставка' in message.text.lower():
        bot.send_message(message.chat.id, 'Формат запроса:\n"Ключевая ставка <СТРАНЫ>"')

    elif 'нефть' in message.text.lower() or 'нефти' in message.text.lower():
        v = 'oil'
        bot.send_message(message.chat.id, f'🛢 Фьючерс на нефть\n<b>Brent</b>:  {econ_ind(v)[0][:7].strip()} $/баррель'
                                          f' ({econ_ind(v)[0][-8:].strip()})\n<b>WTI</b>:'
                                          f' {econ_ind(v)[1][:7].strip()} $/баррель'
                                          f' ({econ_ind(v)[1][-8:].strip()})', parse_mode='html')

    # неверный запрос
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю 😞', parse_mode='html')
        with open('requests.txt', 'a', encoding='utf-8') as file:
            file.write('----')
    # мониторинг зопросов
    with open('requests.txt', 'a', encoding='utf-8') as file:
        file.write(f'{message.from_user.first_name} {message.from_user.last_name},{message.text}\n')


if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except Exception as e:
       print(e)
       time.sleep(3)

