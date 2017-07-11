import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
import os
import asyncio


class MomoisAwesome:
    #Requests from August
    def __init__(self, bot):
            self.bot = bot

    @commands.command(pass_context=True)
    async def dispatch(self, ctx):
        author = ctx.message.author
        commandmsg = "```"
        commandmsg += "--- AUGUSTIN ALLIANCE ---\n"
        commandmsg += "aa_info : Master dispatch\n"
        commandmsg += "aa_foreign : Foreign relations\n"
        commandmsg += "aa_member: Member regions\n"
        commandmsg += "aa_ranks : Standardized ranks\n"
        commandmsg += "ref : Reference Desk\n"
        commandmsg += "about_endos : About Endorsements\n"
        commandmsg += "about_inf : About Influence\n"
        commandmsg += "about_building : Basics of Region-Building\n"
        commandmsg += "about_controls : Regional Controls Documentation\n"
        commandmsg += "about_recruit : Illustrated Guide to Recruiting\n"
        commandmsg += "ns_stats : Nation Statistics List\n"
        commandmsg += "jtf _info: Joint Task Force\n"
        commandmsg += "jtf_ophist : JTF operational history\n"
        commandmsg += "jtf_opsec : JTF operational security\n\n"
        commandmsg += "--- CONCH KINGDOM ---\n"
        commandmsg += "ck_info : Information Center\n"
        commandmsg += "ck_govt : Government\n"
        commandmsg += "ck_hist : History\n"
        commandmsg += "ck_map : Map\n"
        commandmsg += "ck_reg : Resident Registry\n"
        commandmsg += "ck_stats : Statistics Office\n\n"
        commandmsg += "--- CAPE OF GOOD HOPE ---\n"
        commandmsg += "cgh_info : Information Center\n"
        commandmsg += "cgh_govt : Charter\n"
        commandmsg += "cgh_hist : History\n"
        commandmsg += "cgh_map : Map\n"
        commandmsg += "cgh_reg : Resident Registry\n"
        commandmsg += "cgh_stats : Statistics Office\n\n"
        commandmsg += "--- RIDGEFIELD ---\n"
        commandmsg += "rf_info : Information Center\n"
        commandmsg += "rf_govt : Statutory Code\n"
        commandmsg += "rf_hist : History\n"
        commandmsg += "rf_map : Map\n"
        commandmsg += "rf_stats : Statistics Office\n\n"
        commandmsg += "--- NARNIA ---\n"
        commandmsg += "na_info : Information Center\n"
        commandmsg += "na_govt : Government\n"
        commandmsg += "na_hist : History\n"
        commandmsg += "na_map : Map\n"
        commandmsg += "na_reg : Resident Registry\n"
        commandmsg += "na_stats : Statistics Office\n\n"
        commandmsg += "--- LAND'S END ---\n"
        commandmsg += "le_info : Information Center\n"
        commandmsg += "le_govt : Corporate\n"
        commandmsg += "le_hist : History\n"
        commandmsg += "le_map : Map\n"
        commandmsg += "le_reg : Resident Registry\n"
        commandmsg += "le_stats : Statistics Office"
        commandmsg += "```"
        
        await self.bot.send_message(member, commandmsg)
                                
    @commands.command(pass_content=True)
    async def commands(self, ctx):
        author = ctx.message.author

            #The first message block
        helpmsgone = "```"
        helpmsgone += "     AUDIO\n\n"
        helpmsgone += "  Command      Syntax                           Description\n"
        helpmsgone += "------------------------------------------------------------\n"
        helpmsgone += "  play         !play term                       Plays the first search result or a link.\n"
        helpmsgone += "  pause        !pause                           Pauses the song currently playing.\n"
        helpmsgone += "  resume       !resume                          Resumes a paused song.\n"
        helpmsgone += "  prev         !prev                            Goes back to the last song.\n"
        helpmsgone += "  repeat       !repeat                          Toggles loop.\n"
        helpmsgone += "  shuffle      !shuffle                         Shuffles the current queue.\n"
        helpmsgone += "  queue        !queue term                      Queues a song to play next.\n"
        helpmsgone += "  skip         !skip                            Skips a song. 50% of listeners must vote to skip.\n"
        helpmsgone += "  song         !song                            Provides info about the current song.\n"
        helpmsgone += "  yt           !yt term                         Searches and plays a video from YouTube."
        helpmsgone += "```"

            #The second block
        helpmsgtwo = "```"
        helpmsgtwo += "     GENERAL\n\n"
        helpmsgtwo += "  Command      Syntax                           Description\n"
        helpmsgtwo += "------------------------------------------------------------\n"
        helpmsgtwo += "  8            !8 Question?                     Ask the 8 ball a question.\n"
        helpmsgtwo += "  choose       !choose option1 option2          Chooses between multiple choices.\n"
        helpmsgtwo += "  flip         !flip @user                      Flips a coin. Flips a user if one is entered.\n"
        helpmsgtwo += "  poll         !poll Question?;option1;option2  Starts or stops a poll.\n"
        helpmsgtwo += "  roll         !roll #limit                     Rolls a random number. Upper bound is #limit if one is entered.\n"
        helpmsgtwo += "  rps          !rps choice (rock, etc)          Play rock-paper-scissors.\n"
        helpmsgtwo += "  stopwatch    !stopwatch                       Starts and stops a stopwatch.\n"
        helpmsgtwo += "  trivia       !trivia list                     Starts a trivia session with the specified list\n"
        helpmsgtwo += "  zalgo        !zalgo #size (1-7) text          HE COMES\n"
        helpmsgtwo += "  serverinfo   !serverinfo                      Shows information about the server.\n"
        helpmsgtwo += "  userinfo     !userinfo @user                  Shows information about a user.
        helpmsgtwo += "```"

            #The third block
        helpmsgthree = "```"
        helpmsgthree += "     NATIONSTATES\n\n"
        helpmsgthree += "  Command      Syntax                           Description\n"
        helpmsgthree += "------------------------------------------------------------\n"
        helpmsgthree += "  nation       !nation name                     Retrieves info about a nation.\n"
        helpmsgthree += "  region       !region name                     Retrieves info about a region.\n"
        helpmsgthree += "  ne           !ne name                         Displays the nations endorsing a specific WA nation.\n"
        helpmsgthree += "  nec          !nec name                        Counts the number of nations endorsing a specific WA nation.\n"
        helpmsgthree += "  nne          !nne name                        Displays the nations not endorsing a specific WA nation.\n"
        helpmsgthree += "  nnec         !nnec name                       Counts the number of nations not endorsing a specific WA nation.\n"
        helpmsgthree += "  spdr         !spdr name                       Displays the raw influence value of a specific nation.\n"
        helpmsgthree += "  ga           !ga                              Retrieves info on the current GA resolution.\n"
        helpmsgthree += "  sc           !sc                              Retrieves info on the current SC resolution.\n"
        helpmsgthree += "  shard        !shard n/r specific              Retrieves info from a specific API shard."
        helpmsgthree += "```"

        await self.bot.send_message(member, helpmsgone)
        await self.bot.send_message(member, helpmsgtwo)
        await self.bot.send_message(member, helpmsgthree)

def setup(bot):
    bot.add_cog(MomoisAwesome(bot))
