from minecraft import *
from time import sleep
# Minecraftに接続
mc = Minecraft.create()
# プレイヤーの現在位置を取得
player_pos = mc.player.getTilePos()
# ブロックを配置する位置を計算
block_pos = Vec3(player_pos.x + 1, player_pos.y, player_pos.z)
# ブロックを配置
mc.setBlock(block_pos.x, block_pos.y, block_pos.z, BLOCK_STONE)
# 3秒待機
sleep(3)
# ブロックを削除
mc.setBlock(block_pos.x, block_pos.y, block_pos.z, BLOCK_AIR)
