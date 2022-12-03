import pywhatkit as kit
import locale


locale.setlocale(locale.LC_ALL, "Turkish_Turkey.1254")

number ="+905524468203"

kit.sendwhatmsg(number, "A-", 16, 21)