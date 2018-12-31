import config

def check_if_staff(ctx):
    return False


def check_if_bot_manager(ctx):
    return False

def check_if_staff_or_ot(ctx):
    if not ctx.guild:
        return True
    is_meme = (ctx.channel.name == "meme_line" || ctx.channel.name == "modding_irl")
    return is_meme
