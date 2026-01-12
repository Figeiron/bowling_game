class Round:
    def __init__(self, kick, triangle):
        self.kicks_counter = 0
        self.kick = kick
        self.triangle = triangle

    def run(self):
        print("\n!!! РАУНД ПОЧАВСЯ !!!")
        self.triangle.print_pins()
        
        for i in range(1, 3):
            self.kicks_counter = i
            print(f"\nКидок {i}:")
            self.kick.run()
            self.triangle.print_pins()

            if all(pin.is_knocked for pin in self.triangle.pins):
                if i == 1:
                    print("\n!!! STRIKE !!!")
                else:
                    print("\n!!! SPARE !!!")
                return

        remaining = sum(1 for p in self.triangle.pins if not p.is_knocked)
        if remaining > 0:
            print(f"\nРаунд завершено. Залишилося кеглів: {remaining}")
        else:
            pass
        