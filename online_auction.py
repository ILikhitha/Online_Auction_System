class AuctionItem:
    def __init__(self, item_name, start_price):
        self.item_name = item_name
        self.current_price = start_price
        self.highest_bidder = None

    def place_bid(self, bidder_name, bid_amount):
        if bid_amount > self.current_price:
            self.current_price = bid_amount
            self.highest_bidder = bidder_name
            return True
        else:
            return False

class Auction:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, start_price):
        item = AuctionItem(item_name, start_price)
        self.items.append(item)

    def list_items(self):
        for idx, item in enumerate(self.items):
            print(f"{idx + 1}. {item.item_name} - Current Price: ${item.current_price} - Highest Bidder: {item.highest_bidder}")

    def bid_on_item(self, item_index, bidder_name, bid_amount):
        if 0 <= item_index < len(self.items):
            item = self.items[item_index]
            if item.place_bid(bidder_name, bid_amount):
                print(f"Bid of ${bid_amount} placed on {item.item_name} by {bidder_name}")
            else:
                print(f"Bid of ${bid_amount} is too low for {item.item_name}. Current Price: ${item.current_price}")
        else:
            print("Invalid item index.")

# Example Usage
def main():
    auction = Auction()
    auction.add_item("Antique Vase", 100)
    auction.add_item("Vintage Watch", 150)
    auction.add_item("Painting by Van Gogh", 1000)

    while True:
        print("\nItems available for auction:")
        auction.list_items()

        choice = input("\nEnter the item number to place a bid or 'q' to quit: ")
        if choice.lower() == 'q':
            break

        try:
            item_index = int(choice) - 1
            bidder_name = input("Enter your name: ")
            bid_amount = float(input("Enter your bid amount: $"))

            auction.bid_on_item(item_index, bidder_name, bid_amount)
        except ValueError:
            print("Invalid input. Please enter the correct item number and bid amount.")

if __name__ == "__main__":
    main()
