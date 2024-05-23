from abc import ABC, abstractmethod


def minable_required(method):
    def wrapper(self, *args, **kwargs):
        if not self.minable:
            print(f"Криптовалюту {self.name} ({self.symbol}) майнить нельзя.")
            return None
        return method(self, *args, **kwargs)
    return wrapper


class Cryptocurrency(ABC):
    def __init__(self, name, symbol, minable, rate_to_usd, anonymous):
        self.name = name
        self.symbol = symbol
        self.minable = minable
        self.rate_to_usd = rate_to_usd
        self.anonymous = anonymous

    @abstractmethod
    def mining_reward(self):
        pass


class Nano(Cryptocurrency):
    def __init__(self, block_lattice, rate_to_usd, anonymous):
        super().__init__('Nano', 'NANO', True, rate_to_usd, anonymous)
        self.block_lattice = block_lattice

    @minable_required
    def mining_reward(self):
        return 0.02


class Iota(Cryptocurrency):
    def __init__(self, tangle, rate_to_usd, anonymous):
        super().__init__('Iota', 'IOTA', True, rate_to_usd, anonymous)
        self.tangle = tangle

    @minable_required
    def mining_reward(self):
        return 0.001


class Stellar(Cryptocurrency):
    def __init__(self, distributed, rate_to_usd, anonymous):
        super().__init__('Stellar', 'XLM', False, rate_to_usd, anonymous)
        self.distributed = distributed

    @minable_required
    def mining_reward(self):
        return 0


def print_info(crypto):
    minable_str = "добывают майнингом" if crypto.minable else "не майнится"
    anonymous_str = "анонимные транзакции" if crypto.anonymous else "только публичные транзакции"
    extra_str = ""
    if isinstance(crypto, Nano):
        extra_str = ", блок-решетка" if crypto.block_lattice else ""
    print(f"{crypto.name} ({crypto.symbol}): {minable_str}, курс к USD: {crypto.rate_to_usd}, {anonymous_str}{extra_str}")


cryptocurrencies = [Nano(block_lattice=True, rate_to_usd=6, anonymous=False),
                    Iota(tangle=True, rate_to_usd=0.4, anonymous=False),
                    Stellar(distributed=False, rate_to_usd=0.15, anonymous=True)]

for crypto in cryptocurrencies:
    print_info(crypto)
    if crypto.minable:
        print(f"Награда за майнинг: {crypto.mining_reward()} {crypto.symbol}\n")