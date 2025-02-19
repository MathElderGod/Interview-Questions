import java.util.Map;
import java.util.HashMap;

/**
 * cite: 	https://stackoverflow.com/questions/2594059/removing-all-items-of-a-given-value-from-a-hashmap
 * 		https://docs.oracle.com/javase/8/docs/api/java/util/Map.html
 * 		https://docs.oracle.com/javase/8/docs/api/java/util/HashMap.html
 */

public class BestBuy implements ItemStore {

	// private intance variable to store the current items
	// Map Data structure
	private Map<String, Item> currentItems;

	/**
	 * Constructor for Best Buy
	 *
	 * initialize a new list of current store items
	 */
	public BestBuy(){
		this.currentItems = new HashMap<String, Item>();
	}
	
	/** 
	 * Adds an {@link Item} to the store, replacing any existing item with the
	 * same {@link Item#id} value.
	 *
	 * @param item the item to be put into the list of current items
	 */
	@Override
	public void put(Item item) {
		this.currentItems.put(item.getID(), item);
	}

	/**
	 *  Retrieves the {@link Item} with the given {@link Item#id} value, or
	 *  null if no such {@link Item} exists in the store.
	 *  
	 *  @param id the item id
	 *  @return the current item associated with the id passed in
	 */
	@Override
	public Item get(String id){
		return this.currentItems.get(id);
	}

	/**
	 * Delete all {@link Item}s with the specified tag.
	 *
	 * @param tag the item tag
	 */

	@Override
	public void dropAllByTag(String tag){
		// remove all values from the hashmap if the value has
		// the same tag as the parameter 
		currentItems.values().removeIf(val -> tag.equals(val.getTag()));
	}

	/**
	 * Returns the number of Items in the store
	 * @return the number of current items 
	 */
	@Override 
	public int size(){
		return currentItems.size();
	}

	/**
	 * function to print all current items
	 */
	public void printCurrentItems(){
		System.out.println("The current stock is: ");
		for(Map.Entry<String, Item> someItem : this.currentItems.entrySet()){
			System.out.println("Item: " + someItem.getValue().getID() + " | " + someItem.getValue().getTag());
		}
	}

	// Implement the item interface
	public static class BestBuyItem implements Item {
		// private instance variables to store id and tag
		private String id;
		private String tag;

		/**
		 * Constructor for best buy items
		 *
		 * @param id the string id
		 * @param tag the string tag
		 */
		public BestBuyItem(String id, String tag){
			this.id = id;
			this.tag = tag;
		}
		/**
		 * Accessor method. Simply return the items id
		 *
		 * @return item id
		 */
		@Override
		public String getID(){
			return this.id;
		}
		
		/**
		 * Accessor method. Simply return the items tag
		 *
		 * @return item tag
		 */
		@Override
		public String getTag(){
			return this.tag;
		}
	}

	public static void main(String args[]){
		BestBuy bestBuyStore = new BestBuy();
		// test the put method from bestbuystore
		bestBuyStore.put(new BestBuyItem("A123", "Laptop - Dell Inspiron 15"));
        	bestBuyStore.put(new BestBuyItem("B456", "Smartphone - Samsung Galaxy S23"));
        	bestBuyStore.put(new BestBuyItem("C789", "Headphones - Sony WH-1000XM5"));
        	bestBuyStore.put(new BestBuyItem("D012", "Smart TV - LG 65\" OLED"));
        	bestBuyStore.put(new BestBuyItem("E345", "Gaming Console - PlayStation 5"));
        	bestBuyStore.put(new BestBuyItem("F678", "Tablet - Apple iPad Pro 11\""));
        	bestBuyStore.put(new BestBuyItem("G901", "Smartwatch - Apple Watch Series 8"));
        	bestBuyStore.put(new BestBuyItem("H234", "Camera - Nikon D3500 DSLR"));
        	bestBuyStore.put(new BestBuyItem("I567", "External Hard Drive - Seagate 2TB"));
        	bestBuyStore.put(new BestBuyItem("J890", "Bluetooth Speaker - JBL Charge 5"));
		// should be 10 items
		System.out.println("The current stock is: " +  bestBuyStore.size());
		// replace an item
		bestBuyStore.put(new BestBuyItem("H234", "Wireless Mouse - Logitech MX Master 3"));
		// should still print 10 
		System.out.println("The current stock is: " +  bestBuyStore.size());
		// add items of the same exact tag
		bestBuyStore.put(new BestBuyItem("H234", "Camera - Nikon D3500 DSLR"));
		bestBuyStore.put(new BestBuyItem("H235", "Camera - Nikon D3500 DSLR"));
		bestBuyStore.put(new BestBuyItem("H236", "Camera - Nikon D3500 DSLR"));
		bestBuyStore.put(new BestBuyItem("H237", "Camera - Nikon D3500 DSLR"));
		// should now be 13 items
		System.out.println("The current stock is: " +  bestBuyStore.size());
		bestBuyStore.put(new BestBuyItem("A123", "Camera - Nikon D3500 DSLR"));
		bestBuyStore.put(new BestBuyItem("B456", "Camera - Nikon D3500 DSLR"));
		bestBuyStore.put(new BestBuyItem("C789", "Camera - Nikon D3500 DSLR"));
		bestBuyStore.put(new BestBuyItem("D012", "Camera - Nikon D3500 DSLR"));
		bestBuyStore.put(new BestBuyItem("E345", "Camera - Nikon D3500 DSLR"));
		bestBuyStore.put(new BestBuyItem("F678", "Camera - Nikon D3500 DSLR"));
		bestBuyStore.put(new BestBuyItem("G901", "Camera - Nikon D3500 DSLR"));
		// SHOULD STILL BE 13
		System.out.println("The current stock is: " +  bestBuyStore.size());
		// remove all items given that they have the "Camera - Nikon D3500 DSLR" tag
		bestBuyStore.dropAllByTag("Camera - Nikon D3500 DSLR");
		// this should drop a total of 11 items, meaning we should have 2 items left
		System.out.println("The current stock is: " +  bestBuyStore.size());
		// should print items I567 AND J890
		bestBuyStore.printCurrentItems();
		// try to get an item that does not exist
		Item someItem = bestBuyStore.get("A123");
		// should enter the statement
		if(someItem == null){
			System.out.println("Item with id: A123 does not exist!");
		}
		// should print out the external hard drive item since it is not null
		someItem = bestBuyStore.get("I567");
		System.out.println("Item extracted is: " + someItem.getID() + " | " + someItem.getTag());
		bestBuyStore.put(new BestBuyItem("J890", "External Hard Drive - Seagate 2TB"));
		bestBuyStore.dropAllByTag("External Hard Drive - Seagate 2TB");
		// this should drop a total of 2 items, thus our stock is 0
                System.out.println("The current stock is: " +  bestBuyStore.size());
		// all methods work as intended.
	}
}
