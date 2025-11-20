// ---------------------- Pizza Base Class ----------------------
abstract class Pizza {

    void prepare() {
        System.out.println("Preparing " + getClass().getSimpleName());
    }

    void bake() {
        System.out.println("Baking pizza");
    }

    void cut() {
        System.out.println("Cutting pizza");
    }

    void box() {
        System.out.println("Boxing pizza\n");
    }
}

// ---------------------- Concrete Pizza Types ----------------------
class NYCheesePizza extends Pizza { }

class CHCheesePizza extends Pizza { }

// ---------------------- Pizza Store (Factory Method) ----------------------
abstract class PizzaStore {

    public void orderPizza(String type) {
        Pizza p = createPizza(type);
        p.prepare();
        p.bake();
        p.cut();
        p.box();
    }

    abstract Pizza createPizza(String type);
}

// ---------------------- NY Store ----------------------
class NYStore extends PizzaStore {
    Pizza createPizza(String type) {
        if (type.equals("cheese"))
            return new NYCheesePizza();
        return null;
    }
}

// ---------------------- Chicago Store ----------------------
class CHStore extends PizzaStore {
    Pizza createPizza(String type) {
        if (type.equals("cheese"))
            return new CHCheesePizza();
        return null;
    }
}

// ---------------------- Main Class ----------------------
public class Pizza4 {
    public static void main(String[] args) {

        PizzaStore ny = new NYStore();
        PizzaStore ch = new CHStore();

        ny.orderPizza("cheese");
        ch.orderPizza("cheese");
    }
}
