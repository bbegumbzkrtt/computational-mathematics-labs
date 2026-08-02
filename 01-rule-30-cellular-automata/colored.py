import numpy as np
import matplotlib.pyplot as plt

def generate_rule30(steps=250, width=501):
    # Grid oluştur
    grid = np.zeros((steps, width), dtype=int)
    grid[0, width // 2] = 1

    rule_30 = {
        (1, 1, 1): 0, (1, 1, 0): 0, (1, 0, 1): 0, (1, 0, 0): 1,
        (0, 1, 1): 1, (0, 1, 0): 1, (0, 0, 1): 1, (0, 0, 0): 0
    }

    for t in range(1, steps):
        for i in range(1, width - 1):
            neighborhood = (grid[t - 1, i - 1], grid[t - 1, i], grid[t - 1, i + 1])
            grid[t, i] = rule_30[neighborhood]

    return grid

if __name__ == "__main__":
    # 250 adımlık daha büyük ve detaylı grid
    grid = generate_rule30(steps=250, width=501)

    # Görselleştirme (Dark Mode & Mavi/Neon Renk Paleti)
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # 'YlGnBu' veya 'cool' renk paleti ile harika bir deniz/neon havası
    cax = ax.imshow(grid, cmap='cool', interpolation='nearest')

    ax.set_title("Rule 30 - Deep Ocean & Cyberpunk Edition", fontsize=14, color='cyan', pad=12)
    ax.axis('off')  # Çerçeve ve sayıları kaldırıp tam bir sanat eserine dönüştürelim

    # Klasörün içine yeni isimle kaydet
    output_path = "01-rule-30-cellular-automata/rule_30_ocean_neon.png"
    plt.savefig(output_path, bbox_inches='tight', dpi=300, facecolor=fig.get_facecolor())
    print(f"Harika görsel başarıyla kaydedildi: {output_path}")
