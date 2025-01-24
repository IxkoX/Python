class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        """
        Inicializace bankovního účtu.
        :param account_number: Číslo účtu (str nebo int).
        :param owner: Jméno majitele účtu (str).
        :param balance: Počáteční zůstatek (výchozí hodnota je 0).
        """
        self._account_number = account_number  # Privátní atribut
        self._owner = owner                    # Privátní atribut
        self._balance = balance                # Privátní atribut

    @property
    def account_number(self):
        """Vrací číslo účtu (read-only)."""
        return self._account_number

    @property
    def owner(self):
        """Vrací jméno majitele (read-only)."""
        return self._owner

    @property
    def balance(self):
        """Vrací aktuální zůstatek."""
        return self._balance

    def deposit(self, amount):
        """
        Vloží peníze na účet.
        :param amount: Částka k vložení (kladné číslo).
        """
        if amount <= 0:
            raise ValueError("Nelze vložit zápornou částku nebo nulu.")
        self._balance += amount

    def withdraw(self, amount):
        """
        Odebere peníze z účtu.
        :param amount: Částka k odebrání.
        """
        if amount <= 0:
            raise ValueError("Nelze odebrat zápornou částku nebo nulu.")
        if amount > self._balance:
            raise ValueError("Nedostatečné prostředky na účtu.")
        self._balance -= amount

    def print_balance(self):
        """
        Tiskne aktuální zůstatek na účtu.
        """
        print(f"Číslo účtu: {self._account_number}, Majitel: {self._owner}, Zůstatek: {self._balance}.")

# Specializace - spořicí účet
class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0, interest_rate=0.01):
        """
        Inicializace spořicího účtu.
        :param interest_rate: Roční úroková sazba (výchozí 1%).
        """
        super().__init__(account_number, owner, balance)
        self._interest_rate = interest_rate

    @property
    def interest_rate(self):
        """Vrací úrokovou sazbu."""
        return self._interest_rate

    def add_interest(self):
        """Přidá úrok na základě aktuálního zůstatku."""
        interest = self._balance * self._interest_rate
        self.deposit(interest)

# Příklad použití
if __name__ == "__main__":
    account = BankAccount("123456789", "Jan Novák", 1000)
    account.print_balance()
    account.deposit(500)
    account.withdraw(300)
    account.print_balance()

    savings = SavingsAccount("987654321", "Petr Svoboda", 2000, interest_rate=0.05)
    savings.print_balance()
    savings.add_interest()
    savings.print_balance()
