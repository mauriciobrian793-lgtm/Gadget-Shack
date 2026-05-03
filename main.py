import discord
import datetime
from discord import app_commands

# ================= CONFIG =================

import os
from dotenv import load_dotenv

load_dotenv()

TOKEN        = os.getenv("TOKEN")

GUILD_ID = 1496982899725959328

PROMOTION_CHANNEL_ID = 1500240078180581447
PROMOTIONAL_ROLE_ID = 1496983069532618903
INFRACTION_ROLE_ID = 1496983072011325591
INFRACTION_CHANNEL_ID = 1500240110329794682
MWMR_ROLE_ID = 1496983076155166943
LOG_SALE_CHANNEL_ID = 1500254832597012600
SALE_ASSIGNMENT_CHANNEL_ID = 1500256753625993286
# ================= INTENTS =================

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# ================= CLIENT =================

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# ================= READY =================

@client.event
async def on_ready():
    try:
        await tree.sync(guild=discord.Object(id=GUILD_ID))
        print("===================================")
        print(f"Logged in as {client.user}")
        print("Commands synced.")
        print("Bot is online.")
        print("===================================")
    except Exception as e:
        print(f"Sync error: {e}")

# ================= PROMOTION COMMAND =================

@tree.command(
    name="promotion",
    description="Promote a user to a specified role",
    guild=discord.Object(id=GUILD_ID)
)
async def promotion(
    interaction: discord.Interaction,
    user: discord.Member,
    new_rank: str,
    reason: str,
    notes: str,
    issued_by: discord.Member
):

    # ================= PERMISSION CHECK =================
    if PROMOTIONAL_ROLE_ID not in [role.id for role in interaction.user.roles]:
        await interaction.response.send_message(
            "❌ You do not have permission to use this command.",
            ephemeral=True
        )
        return

    # ================= CHANNEL =================
    channel = client.get_channel(PROMOTION_CHANNEL_ID)

    if channel is None:
        await interaction.response.send_message(
            "❌ Promotion channel not found.",
            ephemeral=True
        )
        return

    # ================= EMBED =================
    embed = discord.Embed(
        title="Mid-Wilshire Real Estates | Promotion",
        color=0x808080,
    )

    embed.add_field(
        name="> Agent being promoted:",
        value=user.mention,
        inline=False
    )

    embed.add_field(
        name="> issued by:",
        value=issued_by.mention,
        inline=False
    )

    embed.add_field(
        name="▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬",
        value="\u200b",
        inline=False
    )

    embed.add_field(
        name="> Reason:",
        value=reason,
        inline=False
    )

    embed.add_field(
        name="> Notes:",
        value=notes,
        inline=False
    )

    embed.add_field(
        name="> Promoted To:",
        value=new_rank,
        inline=False
    )

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/1496982900602835096/1500243417588826162/LARP_MID-WILSHIRE_REAL_ESTATE.webp"
    )

    embed.set_footer(
        text="Your activity and dedication has not gone unnoticed,\n you deserve this promotion, we thank you for your service."
    )

    # ================= SEND =================
    await channel.send(
        content=user.mention,
        embed=embed
    )

    await interaction.response.send_message(
        "✅ Promotion submitted successfully.",
        ephemeral=True
    )

@tree.command(
        name="infraction",
        description="Issue an infraction to a user",
        guild=discord.Object(id=GUILD_ID)
    )
async def infraction(
        interaction: discord.Interaction,
        user: discord.Member,
        infraction_type: str,
        reason: str,
        notes: str,
        proof: str,
        issued_by: discord.Member
    ):

    if INFRACTION_ROLE_ID not in [role.id for role in interaction.user.roles]:
        await interaction.response.send_message(
            "❌ You do not have permission to use this command.",
            ephemeral=True
        )
        return

    channel = client.get_channel(INFRACTION_CHANNEL_ID)

    if channel is None:
        await interaction.response.send_message(
            "❌ Infraction channel not found.",
            ephemeral=True
        )
        return

    embed = discord.Embed(
        title="Mid-Wilshire Real Estates | Infraction",
        color=0x808080,
    )

    embed.add_field(
        name="> Agent receiving infraction:",
        value=user.mention,
        inline=False
    )

    embed.add_field(
        name="> issued by:",
        value=issued_by.mention,
        inline=False
    )
    embed.add_field(
        name="▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="> Infraction Type:",
        value=infraction_type,
        inline=False
    )
    embed.add_field(
        name="> Reason:",
        value=reason,
        inline=False
    )
    embed.add_field(
        name="> Notes:",
        value=notes,
        inline=True
    )
    embed.add_field(
        name="> Proof:",
        value=proof,
        inline=True
    )
    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/1496982900602835096/1500243417588826162/LARP_MID-WILSHIRE_REAL_ESTATE.webp"
    )
    embed.set_footer(
        text="We hope this infraction serves as a reminder to uphold the standards of our community and encourages positive behavior moving forward."
    )
    await channel.send(
        content=user.mention,
        embed=embed
    )
    await interaction.response.send_message(
        "✅ Infraction submitted successfully.",
        ephemeral=True
    )

@tree.command(
        name="log_sale",
        description="Log a property sale",
        guild=discord.Object(id=GUILD_ID)
    )

async def log_sale(
        interaction: discord.Interaction,
        agent: discord.Member,
        property_name: str,
        sale_price: str,
        notes: str,
        proof: str,
        logged_by: discord.Member
    ):

    if MWMR_ROLE_ID not in [role.id for role in interaction.user.roles]:
        await interaction.response.send_message(
            "❌ You do not have permission to use this command.",
            ephemeral=True
        )
        return

    channel = client.get_channel(LOG_SALE_CHANNEL_ID)

    if channel is None:
        await interaction.response.send_message(
            "❌ Sale log channel not found.",
            ephemeral=True
        )
        return

    embed = discord.Embed(
        title="Mid-Wilshire Real Estates | Property Sale",
        color=0x808080,
    )

    embed.add_field(
        name="> Agent:",
        value=agent.mention,
        inline=False
    )

    embed.add_field(
        name="> Logged by:",
        value=logged_by.mention,
        inline=False
    )
    embed.add_field(
        name="▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬",
        value="\u200b",
        inline=False
    )

    embed.add_field(
        name="> Property Name:",
        value=property_name,
        inline=False
    )
    embed.add_field(
        name="> Sale Price:",
        value=sale_price,
        inline=False
    )
    embed.add_field(
        name="> Notes:",
        value=notes,
        inline=True
    )
    embed.add_field(
        name="> Proof:",
        value=proof,
        inline=True
    )
    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/1496982900602835096/1500243417588826162/LARP_MID-WILSHIRE_REAL_ESTATE.webp"
    )
    embed.set_footer(
        text="Congratulations on your successful sale! Your dedication and hard work are truly commendable, and we look forward to seeing more of your achievements in the future."
    )
    await channel.send(
        content=agent.mention,
        embed=embed
    )
    await interaction.response.send_message(
        "✅ Sale logged successfully.",
        ephemeral=True
    )

@tree.command(
        name="assign_buyer",
        description="Assign a Agent to help a buyer",
        guild=discord.Object(id=GUILD_ID)
    )

async def assign_buyer(
        interaction: discord.Interaction,
        agent: discord.Member,
        buyer_name: str,
        property_type: str,
        notes: str,
        channel_link: str,
        assigned_by: discord.Member
    ):

    if MWMR_ROLE_ID not in [role.id for role in interaction.user.roles]:
        await interaction.response.send_message(
            "❌ You do not have permission to use this command.",
            ephemeral=True
        )
        return

    channel = client.get_channel(SALE_ASSIGNMENT_CHANNEL_ID)

    if channel is None:
        await interaction.response.send_message(
            "❌ Sale assignment channel not found.",
            ephemeral=True
        )
        return

    embed = discord.Embed(
        title="Mid-Wilshire Real Estates | Buyer Assignment",
        color=0x808080,
    )

    embed.add_field(
        name="> Agent:",
        value=agent.mention,
        inline=False
    )

    embed.add_field(
        name="> Assigned by:",
        value=assigned_by.mention,
        inline=False
    )
    embed.add_field(
        name="▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="> Buyer Name:",
        value=buyer_name,
        inline=False
    )
    embed.add_field(
        name="> Property Type:",
        value=property_type,
        inline=False
    )

    embed.add_field(
        name="> Notes:",
        value=notes,
        inline=True
    )
    embed.add_field(
        name="> Channel Link:",
        value=channel_link,
        inline=True
    )
    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/1496982900602835096/1500243417588826162/LARP_MID-WILSHIRE_REAL_ESTATE.webp"
    )
    embed.set_footer(
        text="If you are available to assist this buyer, please reach out to the agent that assigned youas soon as possible. Your support and dedication to our clients are greatly appreciated."
    )

    await interaction.response.send_message(
        "✅ Sale logged successfully.",
        ephemeral=True
    )

    await channel.send(
        content=f"<@&{MWMR_ROLE_ID}>",
        embed=embed
    )

@tree.command(
    name="promote_test",
    description="Test promotion command",
    guild=discord.Object(id=GUILD_ID)
)
async def promote_test(
    interaction: discord.Interaction,
    staff_member: discord.Member,
    new_rank: str,
    reason: str,
    notes: str
):

    channel = client.get_channel(PROMOTION_CHANNEL_ID)

    if channel is None:
        await interaction.response.send_message(
            "❌ Promotion channel not found.",
            ephemeral=True
        )
        return

    embed = discord.Embed(
    description="## <:lapd:1404775644558131332> Staff Promotion",
    color=0x808080,
)
    embed.add_field(
        name="▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬",
        value="\u200b",
        inline=False
    )

    embed.add_field(
        name="> Staff:",
        value=staff_member.mention,
        inline=False
    )

    embed.add_field(
        name="> New Rank:",
        value=new_rank,
        inline=False
    )

    embed.add_field(
        name="> Reason:",
        value=reason,
        inline=False
    )

    embed.add_field(
        name="> Notes:",
        value=notes,
        inline=False
    )

    embed.set_image(
        url="https://media.discordapp.net/attachments/1500225732599877765/1500361590942335056/1aedbeeb-2a88-4223-8383-ecd54ea7fe38.png?ex=69f8281e&is=69f6d69e&hm=15d29b0be7e98458b4063dea01e2d5a4b44998d91940de8e950a4dacc019e2b9&=&format=webp&quality=lossless&width=688&height=244"
    )

    embed.add_field(
        name="▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬",
        value="\u200b",
        inline=False
    )

    embed.set_footer(
        text="Congratulations on your promotion! Your hard work and dedication have truly paid off, and we look forward to seeing you excel in your new role."
    )

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/1186722448612270187/1500362520978919554/960px-Seal_of_the_Los_Angeles_Police_Department.png?ex=69f828fc&is=69f6d77c&hm=6e4bbcefb1c55ab8effbb01f2116682d8e39b3eb08ed6751aeabf28d297483f5&=&format=webp&quality=lossless&width=833&height=825"
    )

    await channel.send(
        content=staff_member.mention,
        embed=embed
    )

    await interaction.response.send_message(
        "✅ Promotion sent successfully.",
        ephemeral=True
    )
    
# ================= RUN BOT ================

client.run(TOKEN)