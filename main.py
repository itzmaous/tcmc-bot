import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import json
import os
import re
import time

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

class BangGiaDropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="YouTube Premium", description="Xem giá YouTube Premium"),
            discord.SelectOption(label="Capcut Pro", description="Xem giá CapCut Pro"),
            discord.SelectOption(label="Netflix Premium", description="Xem giá Netflix"),
            discord.SelectOption(label="Canva Pro", description="Xem giá Canva Pro"),
            discord.SelectOption(label="Spotify Premium", description="Xem giá Spotify Premium"),
            discord.SelectOption(label="Discord Account", description="Xem giá Discord Account"),
        ]
        super().__init__(placeholder="Xem bảng giá của các sản phẩm....", options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)  # ✅ fix lỗi 10062

        selected = self.values[0]

        if selected == "Capcut Pro":
            embed = discord.Embed(
                title="Bảng Giá Của CapCut Pro",
                description="**GÓI GIÁ DÙNG RIÊNG:**",
                color=0xe0e0e0
            )
            embed.set_author(name="TcMc Store", icon_url="https://cdn.discordapp.com/attachments/1386581458147086468/1386585193514537020/Messenger_creation_2344376032626385.jpg")
            embed.add_field(name="Gói 7 Ngày", value="• > ~~68.000~~đ | **22.000đ** Bank | 30.000đ Card", inline=False)
            embed.add_field(name="Gói 1 Tháng", value="• > ~~100.000~~đ | **50.000đ** Bank | 60.000đ Card", inline=False)
            embed.add_field(name="Gói 1 Năm", value="• > ~~1.000.000~~đ | **340.000đ** Bank | 400.000đ Card", inline=False)
            embed.set_image(url="https://cdn.discordapp.com/attachments/1362943417662836857/1365666647322398771/IMG_8495.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1331484119221407856.png")
            embed.set_footer(text="Coded By Lucifer Maous")

            view = discord.ui.View()
            view.add_item(discord.ui.Button(label="Mua ngay", style=discord.ButtonStyle.link, url="https://discord.com/channels/1370043273145749687/1385270674171629668"))
            await interaction.followup.send(embed=embed, view=view, ephemeral=True)
            return

        elif selected == "YouTube Premium":
            embed = discord.Embed(
                title="Bảng Giá Của YouTube Premium",
                description="**GÓI GIÁ DÙNG RIÊNG:**",
                color=0xFF0000
            )
            embed.set_author(name="TcMc Store", icon_url="https://cdn.discordapp.com/attachments/1386581458147086468/1386585193514537020/Messenger_creation_2344376032626385.jpg")
            embed.add_field(name="Gói 1 Tháng", value="• > ~~50.000~~đ | **30.000đ** Bank | 35.000đ Card", inline=False)
            embed.add_field(name="Gói 3 Tháng", value="• > ~~90.000~~đ | **79.000đ** Bank | 90.000đ Card", inline=False)
            embed.add_field(name="Gói 1 Năm", value="• > ~~360.000~~đ | **299.000đ** Bank | 330.000đ Card", inline=False)
            embed.set_image(url="https://cdn.discordapp.com/attachments/1362943417662836857/1362959386221482176/Ten_Du_an_8.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1284687531723456616.png")
            embed.set_footer(text="Coded By Lucifer Maous")

            view = discord.ui.View()
            view.add_item(discord.ui.Button(label="Mua ngay", style=discord.ButtonStyle.link, url="https://discord.com/channels/1370043273145749687/1385270674171629668"))
            await interaction.followup.send(embed=embed, view=view, ephemeral=True)
            return

        elif selected == "Netflix Premium":
            embed = discord.Embed(
                title="Bảng Giá Của Premium Ultra HD 4K",
                description="**GÓI GIÁ DÙNG RIÊNG:**",
                color=0xE50914
            )
            embed.set_author(name="TcMc Store", icon_url="https://cdn.discordapp.com/attachments/1386581458147086468/1386585193514537020/Messenger_creation_2344376032626385.jpg")
            embed.add_field(name="Gói 1 Tháng", value="• > ~~100.000~~đ | **50.000đ** Bank | 60.000đ Card", inline=False)
            embed.add_field(name="Gói 3 Tháng", value="• > ~~150.000~~đ | **119.000đ** Bank | 140.000đ Card", inline=False)
            embed.add_field(name="Gói 1 Năm", value="• > ~~1.200.000~~đ | **599.000đ** Bank | 700.000đ Card", inline=False)
            embed.set_image(url="https://cdn.discordapp.com/attachments/1362943417662836857/1364727125302841365/Ten_Du_an_8.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1365485079903735888.png")
            embed.set_footer(text="Coded By Lucifer Maous")

            view = discord.ui.View()
            view.add_item(discord.ui.Button(label="Mua ngay", style=discord.ButtonStyle.link, url="https://discord.com/channels/1370043273145749687/1385270674171629668"))
            await interaction.followup.send(embed=embed, view=view, ephemeral=True)
            return
        
        elif selected == "Canva Pro":
            embed = discord.Embed(
                title="Bảng Giá Của Canva Pro",
                description="**GÓI GIÁ DÙNG RIÊNG:**",
                color=0x03befc
            )
            embed.set_author(name="TcMc Store", icon_url="https://cdn.discordapp.com/attachments/1386581458147086468/1386585193514537020/Messenger_creation_2344376032626385.jpg")
            embed.add_field(name="Gói 1 Tháng", value="• > ~~50.000~~đ | **30.000đ** Bank | 40.000đ Card", inline=False)
            embed.add_field(name="Gói 1 Năm", value="• > ~~1.000.000~~đ | **200.000đ** Bank | 240.000đ Card", inline=False)
            embed.set_image(url="https://cdn.discordapp.com/attachments/1362943417662836857/1364728218388791358/Ten_Du_an_8.png?ex=685b2532&is=6859d3b2&hm=30ea2548c7b5b663ab119ab845e2577a89672f44481a258e1758bdb67c400d59&")
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1331482278928580731.png")
            embed.set_footer(text="Coded By Lucifer Maous")

            view = discord.ui.View()
            view.add_item(discord.ui.Button(label="Mua ngay", style=discord.ButtonStyle.link, url="https://discord.com/channels/1370043273145749687/1385270674171629668"))
            await interaction.followup.send(embed=embed, view=view, ephemeral=True)
            return
        
        elif selected == "Spotify Premium":
            embed = discord.Embed(
                title="Bảng Giá Của Spotify Premium",
                description="**GÓI GIÁ DÙNG RIÊNG:**",
                color=0x03fc30
            )
            embed.set_author(name="TcMc Store", icon_url="https://cdn.discordapp.com/attachments/1386581458147086468/1386585193514537020/Messenger_creation_2344376032626385.jpg")
            embed.add_field(name="Gói 1 Tháng", value="• > ~100.000~đ | **60.000đ** Bank", inline=False)
            embed.add_field(name="Gói 3 Tháng", value="• > ~150.000~đ | **90.000đ** Bank", inline=False)
            embed.add_field(name="Gói 1 Năm", value="• > ~700.000~đ | **300.000đ** Bank", inline=False)
            embed.set_image(url="https://cdn.discordapp.com/attachments/1362943417662836857/1364727808596770847/Ten_Du_an_8.png?ex=685b24d0&is=6859d350&hm=14cbf37ee28e2c019233f2626617394d3026721380fd0f73388dda53b9854174&")
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1338308799525814353.gif")
            embed.set_footer(text="Coded By Lucifer Maous")

            view = discord.ui.View()
            view.add_item(discord.ui.Button(label="Mua ngay", style=discord.ButtonStyle.link, url="https://discord.com/channels/1370043273145749687/1385270674171629668"))
            await interaction.followup.send(embed=embed, view=view, ephemeral=True)
            return

        elif selected == "Discord Account":
            embed = discord.Embed(
                title="Bảng Giá Của Discord Account",
                description="**GÓI GIÁ DÙNG RIÊNG:**",
                color=0x5468ff
            )
            embed.set_author(name="TcMc Store", icon_url="https://cdn.discordapp.com/attachments/1386581458147086468/1386585193514537020/Messenger_creation_2344376032626385.jpg")
            embed.add_field(name="Discord 2016", value="• > **299.000đ** Bank | 350.000đ Card", inline=False)
            embed.add_field(name="Gói 3 Tháng", value="• > **180.000đ** Bank | 210.000đ Card", inline=False)
            embed.add_field(name="Gói 1 Năm", value="• > **140.000đ** Bank | 170.000đ Card", inline=False)
            embed.add_field(name="Gói 1 Năm", value="• > **100.000đ** Bank | 120.000đ Card", inline=False)
            embed.add_field(name="Gói 1 Năm", value="• > **60.000đ** Bank | 70.000đ Card", inline=False)
            embed.set_image(url="https://media.discordapp.net/attachments/1385435193044897852/1386691005473886279/discord.png?ex=685b48e3&is=6859f763&hm=bed542671df644c4080661d1f9f93b22939b437faa44b2760b6f38bb30c24a0a&=&format=webp&quality=lossless&width=983&height=655")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/1386581458147086468/1386902394704494634/discord_PNG8.png?ex=685b6502&is=685a1382&hm=e9cfbe1b7a12478e20d050879996b69956aec8a717742bd329d1ab07c1222d5c&=&format=webp&quality=lossless&width=655&height=655")
            embed.set_footer(text="Coded By Lucifer Maous")

            view = discord.ui.View()
            view.add_item(discord.ui.Button(label="Mua ngay", style=discord.ButtonStyle.link, url="https://discord.com/channels/1370043273145749687/1385270674171629668"))
            await interaction.followup.send(embed=embed, view=view, ephemeral=True)
            return

        else:
            embed = discord.Embed(
                title="❌ Không tìm thấy sản phẩm",
                description="Vui lòng chọn lại.",
                color=discord.Color.red()
            )

        await interaction.followup.send(embed=embed, ephemeral=True)

class BangGiaView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(BangGiaDropdown())

CATEGORY_A_ID = 1384100770453913650  # Category theo dõi kênh mới tạo
CATEGORY_B_ID = 1370054068159910030  # Category để lấy danh sách kênh
EXCLUDED_CHANNEL_IDS = [1382321425117085767, 1382325718280573088, 1382325249776816139]
DATA_FILE = "account-stock.json"
ADMIN_CHANNEL_ID = 1386605699236237363
ROLE_ID = 1370246387266228244

class DropdownAutoBuy(discord.ui.Select):
    def __init__(self, channels):
        options = [
            discord.SelectOption(label=ch.name, value=str(ch.id)) 
            for ch in channels 
            if "❌" not in ch.name and ch.id not in EXCLUDED_CHANNEL_IDS
        ]
        super().__init__(placeholder="Chọn tài khoản muốn mua...", options=options, min_values=1, max_values=1)

    async def callback(self, interaction: discord.Interaction):
        selected_channel_id = int(self.values[0])
        channel = interaction.guild.get_channel(selected_channel_id)
        if not channel:
            await interaction.response.send_message("❌ Kênh không tồn tại.", ephemeral=True)
            return

        if not os.path.exists(DATA_FILE):
            await interaction.response.send_message("❌ Dữ liệu stock chưa có.", ephemeral=True)
            return

        with open(DATA_FILE, "r", encoding="utf-8") as f:
            stock_data = json.load(f)

        account = next((acc for acc in stock_data if acc["channel_id"] == selected_channel_id), None)
        if not account:
            await interaction.response.send_message("❌ Không tìm thấy tài khoản liên kết với kênh này.", ephemeral=True)
            return

        if account.get("sold", False):
            await interaction.response.send_message("❌ Tài khoản này đã được bán rồi.", ephemeral=True)
            return

        # Đánh dấu sold = True trong file JSON
        for acc in stock_data:
            if acc["channel_id"] == selected_channel_id:
                acc["sold"] = True
                break

        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4, ensure_ascii=False)

        bank = account.get("bank", "Không rõ").lower()

        channel_name = channel.name

        money_match = re.search(r"(\d+[kKđĐ])", channel_name)
        money = money_match.group(1) if money_match else "Không rõ"

        content_match = re.search(r"\d+[kKđĐ][\-\s]*(.*)", channel_name)
        content = content_match.group(1).replace("-", " ").strip() if content_match else ""

        payment_content = f"{bank.capitalize()} {content}".strip()

        embed = discord.Embed(
            title="💸 Vui lòng thanh toán bank qua số tài khoản sau:",
            color=discord.Color.green()
        )
        embed.add_field(name="Số tiền:", value=f"```{money}```", inline=False)
        embed.add_field(name="Nội dung:", value=f"```{payment_content}```", inline=False)

        bank_logos = {
            "tcuong": "https://cdn.discordapp.com/attachments/1364591729755295806/1377876106647965696/IMG_20250519_205004.jpg",
            "trung": "https://cdn.discordapp.com/attachments/1371313863857016874/1376772845413077103/Screenshot_20250527-110314.png",
        }
        logo_url = bank_logos.get(bank)
        if logo_url:
            embed.set_image(url=logo_url)

        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1386581458147086468/1386585193514537026385/Messenger_creation_2344376032626385.jpg")

        await interaction.response.send_message(
            embed=embed,
            view=ConfirmPaymentView(
                buyer=interaction.user,
                account_data=account,
                money=money,
                payment_content=payment_content,
                channel_name=channel_name
            ),
            ephemeral=True
        )

class DropdownAutoBuyView(discord.ui.View):
    def __init__(self, channels: list[discord.TextChannel]):
        super().__init__(timeout=None)
        self.add_item(DropdownAutoBuy(channels))

class CategoryDropdown(discord.ui.Select):
    def __init__(self, categories, channel_to_move: discord.TextChannel):
        options = [
            discord.SelectOption(label=cat.name, value=str(cat.id))
            for cat in categories
        ]
        super().__init__(placeholder="Chọn category để chuyển kênh sold vào...", options=options, min_values=1, max_values=1)
        self.channel_to_move = channel_to_move

    async def callback(self, interaction: discord.Interaction):
        selected_cat_id = int(self.values[0])
        selected_category = interaction.guild.get_channel(selected_cat_id)

        if not selected_category or not isinstance(selected_category, discord.CategoryChannel):
            await interaction.response.send_message("❌ Category không hợp lệ!", ephemeral=True)
            return

        try:
            await self.channel_to_move.edit(category=selected_category)
            await interaction.response.send_message(
                f"✅ Đã chuyển kênh `{self.channel_to_move.name}` vào category **{selected_category.name}**!",
                ephemeral=True
            )
            self.view.stop()
        except Exception as e:
            await interaction.response.send_message(f"❌ Lỗi khi chuyển kênh: {e}", ephemeral=True)


class CategorySelectView(discord.ui.View):
    def __init__(self, categories, channel_to_move: discord.TextChannel):
        super().__init__(timeout=None)
        self.add_item(CategoryDropdown(categories, channel_to_move))

class SendGuideView(discord.ui.View):
    def __init__(self, buyer: discord.Member):
        super().__init__(timeout=180)
        self.buyer = buyer

    @discord.ui.button(label="Hướng Dẫn Bảo Mật", style=discord.ButtonStyle.primary)
    async def send_guide(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="Yêu cầu khi mua tài khoản!",
            description="Vui lòng làm theo những việc sau khi nhận tài khoản:",
            color=discord.Color.green()
        )
        embed.add_field(
            name="Hướng dẫn bảo mật",
            value='[Hướng dẫn](https://www.youtube.com/watch?v=rRjJmId5oh8)',
            inline=False
        )
        await self.buyer.send(embed=embed)

class AdminApproveView(discord.ui.View):
    def __init__(self, buyer: discord.Member, account_data: dict):
        super().__init__(timeout=None)
        self.buyer = buyer
        self.account_data = account_data

    @discord.ui.button(label="✅ Xác nhận", style=discord.ButtonStyle.success)
    async def approve_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            await interaction.response.defer(ephemeral=True)

            embed = discord.Embed(
                title="📦 Giao dịch thành công!",
                description="Bạn đã nhận được tài khoản như sau:",
                color=discord.Color.green()
            )
            embed.add_field(name="📧 Email", value=f'```{self.account_data.get("email", "Không rõ")}```', inline=False)
            embed.add_field(name="🔑 Recovery Code", value=f'```{self.account_data.get("recovery_code", "Không rõ")}```', inline=False)
            embed.set_footer(text="TcMc Store - Auto Payment System")
            await self.buyer.send(embed=embed)

            channel_id = self.account_data.get("channel_id")
            channel = interaction.guild.get_channel(channel_id)
            channel_name = channel.name if channel else "Không rõ"

            content_match = re.search(r"\d+[kKđĐ][\-\s]*(.*)", channel_name)
            content = content_match.group(1).replace("-", " ").strip() if content_match else "Không rõ"

            bank = self.account_data.get("bank", "Không rõ").lower()
            bank_pings = {
                "tcuong": "<@1258004059210907659>",
                "trung": "<@919508827206991892>",
            }
            ping_id = bank_pings.get(bank, "")
            value = f"+1 legit {ping_id} {content}"

            embed_legit = discord.Embed(
                title="✅ Cộng Legit Cho Store",
                description="Hãy copy và dán vào kênh <#1376136727051112479>",
                color=discord.Color.green()
            )
            embed_legit.add_field(name="Cú Pháp:", value=f"```{value}```", inline=False)
            await self.buyer.send(embed=embed_legit, view=SendGuideView(self.buyer))

            if channel:
                new_name = channel.name.replace("✅", "❌") if "✅" in channel.name else f"❌ {channel.name}"
                await channel.edit(name=new_name)
                categories = interaction.guild.categories
                view = CategorySelectView(categories, channel)
                await interaction.followup.send(
                    "## **Giao dịch thành công**\nVui lòng chọn category để chuyển kênh sold vào:",
                    view=view,
                )
            else:
                await interaction.followup.send("❌ Không tìm thấy kênh để chuyển.", ephemeral=True)

            role = interaction.guild.get_role(ROLE_ID)
            if role:
                await self.buyer.add_roles(role, reason="Đã mua tài khoản")

        except Exception as e:
            await interaction.followup.send(f"❌ Gặp lỗi khi xử lý: `{e}`", ephemeral=True)

    @discord.ui.button(label="❌ Hủy giao dịch", style=discord.ButtonStyle.danger)
    async def cancel_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            await interaction.response.defer(ephemeral=True)

            # Đặt lại sold = False trong file stock
            channel_id = self.account_data.get("channel_id")
            updated = False

            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    stock_data = json.load(f)

                for acc in stock_data:
                    if acc.get("channel_id") == channel_id:
                        acc["sold"] = False
                        updated = True
                        break

                if updated:
                    with open(DATA_FILE, "w", encoding="utf-8") as f:
                        json.dump(stock_data, f, indent=4, ensure_ascii=False)

            # Thông báo cho người mua
            embed = discord.Embed(
                title="❌ Giao dịch đã bị hủy!",
                description="Admin đã từ chối giao dịch. Tài khoản đã được trả lại stock.",
                color=discord.Color.red()
            )
            await self.buyer.send(embed=embed)

            await interaction.followup.send("❌ Giao dịch đã được hủy và thông báo cho người mua.")

        except Exception as e:
            await interaction.followup.send(f"❌ Gặp lỗi khi hủy giao dịch: `{e}`", ephemeral=True)

class ConfirmPaymentView(discord.ui.View):
    def __init__(self, buyer: discord.Member, account_data: dict, money: str, payment_content: str, channel_name: str):
        super().__init__(timeout=None)
        self.buyer = buyer
        self.account_data = account_data
        self.money = money
        self.payment_content = payment_content
        self.channel_name = channel_name

    @discord.ui.button(label="✅ Đã chuyển", style=discord.ButtonStyle.success)
    async def confirm_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            embed=discord.Embed(
                title="✅ Đã ghi nhận chuyển khoản!",
                description="**Vui lòng chờ admin xác nhận giao dịch.**",
                color=discord.Color.green()
            ),
            ephemeral=True
        )

        try:
            admin_channel = interaction.guild.get_channel(ADMIN_CHANNEL_ID)
            if admin_channel:
                embed = discord.Embed(
                    title="📥 Giao Dịch Mới Cần Xác Nhận",
                    description=f"Người mua: {self.buyer.mention}",
                    color=discord.Color.orange()
                )
                embed.add_field(name="Số tiền", value=f"```{self.money}```", inline=False)
                embed.add_field(name="Nội dung", value=f"```{self.payment_content}```", inline=False)
                embed.add_field(name="Kênh", value=f"```{self.channel_name}```", inline=False)
                embed.add_field(name="Bank chủ", value=f"```{self.account_data.get('bank', 'Không rõ').capitalize()}```", inline=False)
                embed.add_field(name="", value="----------------------------------------", inline=False)
                embed.add_field(name="Email", value=f"`{self.account_data.get('email', 'Không rõ')}`", inline=False)
                embed.add_field(name="Recovery Code", value=f"`{self.account_data.get('recovery_code', 'Không rõ')}`", inline=False)
                embed.set_footer(text="TcMc Store - Auto Payment System")

                await admin_channel.send(embed=embed, view=AdminApproveView(self.buyer, self.account_data))

        except Exception as e:
            print(f"Lỗi khi gửi embed admin: {e}")

    @discord.ui.button(label="❌ Hủy bỏ", style=discord.ButtonStyle.danger)
    async def cancel_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel_id = self.account_data.get("channel_id")
        if not channel_id:
            await interaction.response.send_message("❌ Không tìm thấy thông tin kênh để cập nhật.", ephemeral=True)
            return

        # Đọc file JSON stock
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                stock_data = json.load(f)

            # Tìm account theo channel_id và set sold = False
            updated = False
            for acc in stock_data:
                if acc.get("channel_id") == channel_id:
                    acc["sold"] = False
                    updated = True
                    break

            if updated:
                with open(DATA_FILE, "w", encoding="utf-8") as f:
                    json.dump(stock_data, f, indent=4, ensure_ascii=False)

                await interaction.response.send_message(
                    embed=discord.Embed(
                        title="❌ Giao dịch đã bị hủy.",
                        description="Tài khoản đã được trả về trạng thái chưa bán.",
                        color=discord.Color.red()
                    ),
                    ephemeral=True
                )
            else:
                await interaction.response.send_message("❌ Không tìm thấy tài khoản để cập nhật.", ephemeral=True)
        else:
            await interaction.response.send_message("❌ Dữ liệu stock chưa có.", ephemeral=True)
@bot.event
async def on_guild_channel_create(channel: discord.abc.GuildChannel):
    if isinstance(channel, discord.TextChannel) and channel.category_id == CATEGORY_A_ID:
        category_b = channel.guild.get_channel(CATEGORY_B_ID)
        if not category_b or not isinstance(category_b, discord.CategoryChannel):
            return
        
        channels_in_b = [c for c in category_b.channels if isinstance(c, discord.TextChannel)]

        embed = discord.Embed(
            title="Danh sách Tài Khoản Minecraft Đang Có",
            description="Hãy chọn một tài khoản bên dưới để mua:",
            color=discord.Color.blue()
        )
        embed.set_footer(text="TcMc Store - Auto Payment Service")
        time.sleep(0.5)
        await channel.send(embed=embed, view=DropdownAutoBuyView(channels_in_b))


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"✅ Bot đã đăng nhập với tên: {bot.user}")

@bot.tree.command(name="banggia", description="Xem bảng giá các sản phẩm")
async def banggia(interaction: discord.Interaction):
    
    embed = discord.Embed(
        title="📦 Bảng Giá Các Sản Phẩm",
        description="### 🔹 **Nhấn vào nút bên dưới để xem giá sản phẩm**",
        color=discord.Color.purple()
    )
    embed.add_field(
        name="🧾 Store sẽ nhận các phương thức thanh toán như:",
        value="**• > Bank, Card (+20% phí gạch thẻ)**",
        inline=False
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/1386581458147086468/1386587506782240789/1a6ec3245ad0b66777db47fe5297eb90.jpg?ex=685a3fbf&is=6858ee3f&hm=c5d3783b7cfa4a8c2e494f11016377deabc123d09fd50d282f041da683be47ec&")  
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1386581458147086468/1386585193514537020/Messenger_creation_2344376032626385.jpg")
    embed.set_author(name="TcMc Store", icon_url="https://cdn.discordapp.com/attachments/1386581458147086468/1386585193514537020/Messenger_creation_2344376032626385.jpg")

    await interaction.response.send_message(embed=embed, view=BangGiaView(), ephemeral=True)


@bot.tree.command(name="add-account", description="Thêm tài khoản vào stock")
@app_commands.checks.has_permissions(administrator=True)
@app_commands.describe(
    channel="Chọn kênh stock cần liên kết",
    bank="Tên người chủ (vd: tcuong)",
    email="Email tài khoản",
    recovery_code="Recovery code"
)
async def add_account(
    interaction: discord.Interaction,
    channel: discord.TextChannel,
    bank: str,
    email: str,
    recovery_code: str
):
    data = {
        "channel_id": channel.id,
        "bank": bank,
        "email": email,
        "recovery_code": recovery_code
    }

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            existing_data = json.load(f)
    else:
        existing_data = []

    existing_data.append(data)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, indent=4, ensure_ascii=False)

    await interaction.response.send_message(
        f"✅ Đã lưu tài khoản vào stock!\n• Kênh: {channel.mention}\n• Bank: `{bank}`\n• Email: `{email}`",
        ephemeral=True
    )

@bot.tree.command(name="sold", description="Đánh dấu kênh đã bán và chọn category chuyển vào")
@app_commands.describe(channel="Kênh cần đánh dấu đã bán")
@app_commands.checks.has_permissions(administrator=True)
async def sold(interaction: discord.Interaction, channel: discord.TextChannel):
    await interaction.response.defer(ephemeral=True)

    try:
        # Đổi tên kênh
        new_name = channel.name
        if "✅" in new_name:
            new_name = new_name.replace("✅", "❌")
        elif not new_name.startswith("❌"):
            new_name = f"❌ {new_name}"
        await channel.edit(name=new_name)

        # Cập nhật sold: true trong JSON
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                stock_data = json.load(f)

            updated = False
            for acc in stock_data:
                if acc.get("channel_id") == channel.id:
                    acc["sold"] = True
                    updated = True
                    break

            if updated:
                with open(DATA_FILE, "w", encoding="utf-8") as f:
                    json.dump(stock_data, f, indent=4, ensure_ascii=False)

        # Gửi view chọn category
        categories = interaction.guild.categories
        view = CategorySelectView(categories, channel)

        await interaction.followup.send(
            content=f"✅ Đã đánh dấu `{channel.name}` là đã bán và cập nhật dữ liệu.\nVui lòng chọn category để chuyển kênh vào:",
            view=view,
            ephemeral=True
        )

    except Exception as e:
        await interaction.followup.send(f"❌ Gặp lỗi khi xử lý: `{e}`", ephemeral=True)

@add_account.error
async def add_account_error(interaction: discord.Interaction, error):
    if isinstance(error, app_commands.errors.MissingPermissions):
        await interaction.response.send_message("❌ Bạn không có quyền sử dụng lệnh này (chỉ admin được phép).", ephemeral=True)

@sold.error
async def sold_error(interaction: discord.Interaction, error):
    if isinstance(error, app_commands.errors.MissingPermissions):
        await interaction.response.send_message("❌ Bạn không có quyền sử dụng lệnh này (chỉ admin được phép).", ephemeral=True)

bot.run(TOKEN)
