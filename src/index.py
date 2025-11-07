from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    mehua.lisaa_varastoon(50.7)

    mehua.ota_varastosta(3.14)

    olutta.lisaa_varastoon(1000.0)

    mehua.lisaa_varastoon(-666.0)

    print(f"saatiin {olutta.ota_varastosta(1000.0)}")
    print(f"Mehuvarasto: {mehua.ota_varastosta(-32.9)}")

    print("hello")
    print("hello")
    print("hello")
    print("hello")
    print("hello")

if __name__ == "__main__":
    main()
