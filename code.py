# Code to run fireworks animation, then scrolling marquees
# of text surrounded by icons.
# Video to set up this code can be found in the playlist:
# https://bit.ly/pico-school
# Diagram & files/folders at: https://github.com/gallaugher/pico-and-hub75-led-matrix
# Icons are stored in a folder named "graphics" on the CIRCUITPY volume,
# .bdf fonts are stored ina  folder named "fonts"
# For pico use, the "lib" folder needs:
# folders named: adafruit_bitmap_font & adafruit_display_text
# and the library named adafruit_ticks.mpy

import board, displayio, time, gc, random, math, rgbmatrix, framebufferio
# If you use a Matrix Portal S3, you'll need to import the coe below,
# from adafruit_matrixportal.matrixportal import MatrixPortal
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text.label import Label

displayio.release_displays()

# === Setup for Matrix Portal S3 ===
# matrixportal = MatrixPortal(status_neopixel=board.NEOPIXEL, bit_depth=6, debug=True)
# display = matrixportal.graphics.display

# === Setup for Pico ===
# Setup rgbmatrix display (change pins to match your wiring)
matrix = rgbmatrix.RGBMatrix(
    width=64, # Change width & height if you have an LED matrix with different dimensions
    height=32,
    bit_depth=6,
    rgb_pins=[ # Preserve GP4 & GP5 for standard STEMMA-QT
        board.GP2,   # R1
        board.GP3,   # G1
        board.GP6,   # B1
        board.GP7,   # R2
        board.GP8,   # G2
        board.GP9    # B2
    ],
    addr_pins=[
        board.GP10,  # A
        board.GP16,  # B
        board.GP18,  # C
        board.GP20   # D
    ],
    clock_pin=board.GP11,
    latch_pin=board.GP12,
    output_enable_pin=board.GP13,
    tile=1,
    serpentine=False,
    doublebuffer=True,
)

display = framebufferio.FramebufferDisplay(matrix)
# === end of pico setup === #

WIDTH = display.width
HEIGHT = display.height

main_group = displayio.Group()
display.root_group = main_group

# === Fonts ===
font_small = bitmap_font.load_font("/fonts/helvB08.bdf")
font_large = bitmap_font.load_font("/fonts/helvB12.bdf")

# === COLOR VARIABLES ===
WHITE         = 0xFFFFFF
SOFT_RED      = 0xCC4444
DEEP_CORAL    = 0xFF6F61
PEACH         = 0xFFDAB9
WARM_GOLD     = 0xFFD700
GOLDENROD     = 0xDAA520
TANGERINE     = 0xFFA07A

# Lean firework colors toward warm tones
firework_colors = [WHITE, GOLDENROD, WARM_GOLD, DEEP_CORAL, SOFT_RED, TANGERINE]

celebration_colors = [
    WHITE, GOLDENROD, WARM_GOLD, DEEP_CORAL,
    SOFT_RED, TANGERINE, PEACH
]

# === Timing Parameters ===
SCROLL_DELAY = 0.025
SCROLL_STEP = 1

# === Messages: (line1, line2, image_path, optional_color)
# You can add or remove elements from the messages lists, as you like.
# Add a second line of text in the empty strings for a two-line message in smaller font
messages = [
    ("Congratulations Maker!", "", "/graphics/tools.bmp", GOLDENROD),
    ("You Built It!", "", "/graphics/raspberry-pi-logo.bmp", SOFT_RED),
]

def create_scroll_group(logo_path, text1, text2, color=None):
    group = displayio.Group()
    logo_width = 0
    logo_spacing = 33
    logo_tilegrid = None

    if color:
        color1 = color
        color2 = color
    else:
        color1 = random.choice(celebration_colors)
        color2 = random.choice([c for c in celebration_colors if c != color1])

    if logo_path:
        try:
            logo_bitmap = displayio.OnDiskBitmap(logo_path)
            logo_tilegrid = displayio.TileGrid(
                logo_bitmap,
                pixel_shader=logo_bitmap.pixel_shader,
                x=2,
                y=0
            )
            group.append(logo_tilegrid)
            logo_width = logo_tilegrid.width
        except Exception as e:
            print(f"Error loading image {logo_path}: {e}")

    text_start = logo_width + logo_spacing if logo_path else 0

    if text2.strip() == "":
        label1 = Label(font_large, text=text1, color=color1)
        label1.x = text_start
        label1.y = 16
        group.append(label1)
        text_width = label1.bounding_box[2]
    else:
        label1 = Label(font_small, text=text1, color=color1)
        label1.x = text_start
        label1.y = 10
        group.append(label1)

        label2 = Label(font_small, text=text2, color=color2)
        label2.x = text_start
        label2.y = 22
        group.append(label2)

        text_width = max(
            label1.bounding_box[2],
            label2.bounding_box[2]
        )

    total_width = text_start + text_width

    # Add second logo directly after text, no extra spacing
    if logo_path and logo_tilegrid:
        try:
            logo_bitmap = displayio.OnDiskBitmap(logo_path)
            second_logo = displayio.TileGrid(
                logo_bitmap,
                pixel_shader=logo_bitmap.pixel_shader,
                x=text_start + text_width,
                y=0
            )
            group.append(second_logo)
            total_width += second_logo.width + 1  # Ensure full scroll off screen
        except Exception as e:
            print(f"Error loading second logo image: {e}")

    return group, total_width

def fireworks_animation(duration=2.5, burst_count=5, sparks_per_burst=40):
    print("\U0001F386 Multi Fireworks Burst")
    animation_group = displayio.Group()
    main_group.append(animation_group)

    start_time = time.monotonic()
    sparks = []

    for i in range(burst_count):
        cx = random.randint(8, WIDTH - 8)
        cy = random.randint(6, HEIGHT // 2)
        base_color = random.choice(firework_colors)
        launch_delay = i * 0.1

        for _ in range(sparks_per_burst):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(1.5, 3.0)
            dx = speed * math.cos(angle)
            dy = speed * math.sin(angle) - 2.0

            bmp = displayio.Bitmap(1, 1, 1)
            pal = displayio.Palette(1)
            pal[0] = base_color
            pixel = displayio.TileGrid(bmp, pixel_shader=pal, x=cx, y=cy)

            sparks.append({
                "sprite": pixel,
                "x": float(cx),
                "y": float(cy),
                "dx": dx,
                "dy": dy,
                "life": random.randint(15, 25),
                "color": base_color,
                "delay": launch_delay
            })
            animation_group.append(pixel)

    gravity = 0.15

    while time.monotonic() - start_time < duration + 1:
        t = time.monotonic() - start_time
        for spark in sparks:
            if t < spark["delay"]:
                continue

            if spark["life"] <= 0:
                if spark["sprite"] in animation_group:
                    animation_group.remove(spark["sprite"])
                continue

            spark["x"] += spark["dx"]
            spark["y"] += spark["dy"]
            spark["dy"] += gravity
            spark["life"] -= 1

            spark["sprite"].x = int(spark["x"])
            spark["sprite"].y = int(spark["y"])

            fade = spark["life"] / 25
            r = int(((spark["color"] >> 16) & 0xFF) * fade)
            g = int(((spark["color"] >> 8) & 0xFF) * fade)
            b = int((spark["color"] & 0xFF) * fade)
            spark["sprite"].pixel_shader[0] = (r << 16) | (g << 8) | b

        time.sleep(0.05)

    main_group.remove(animation_group)
    gc.collect()

print("*** Running Pico HUB75 Code! ***")

# === Main Loop ===
while True:
    fireworks_animation(duration=2.5, burst_count=3, sparks_per_burst=40)
    for i, (msg1, msg2, logo_path, *optional_color) in enumerate(messages):
        try:
            gc.collect()
            color = optional_color[0] if optional_color else None
            scroll_group, content_width = create_scroll_group(logo_path, msg1, msg2, color)
            scroll_group.x = WIDTH
            main_group.append(scroll_group)

            # while scroll_group.x > -content_width - 1:
            while scroll_group.x > -content_width - 32:
                scroll_group.x -= SCROLL_STEP
                time.sleep(SCROLL_DELAY)

            main_group.remove(scroll_group)
            gc.collect()
            time.sleep(0.5)

        except MemoryError:
            print("\U0001F4A5 MemoryError! Trying to recover...")
            main_group = displayio.Group()
            display.root_group = main_group
            gc.collect()
            time.sleep(1)
