#include <iostream>
using namespace std;

// Sleeping Barber Problem;
// Barber shop with one barber, one barber chair and N chairs to wait in. When no customers the barber goes to sleep in barber chair and must be 
// woken when a customer comes in. When barber is cutting hair new customers take empty seats to wait, or leave if no vacancy. This is basically 
// the Sleeping Barber Problem.

// Solution the Mutex here is the barbers chair and the sphere can have 3 other waiting cut so in sempahore, we have resources shared by these total 
// 4 people

class Shop
{
    bool sleep; // false(not sleeping)
    bool brbr_chair_mutex;
    int avl_chairs;

public:
    Shop()
    {
        sleep = true;
        avl_chairs = 3;
        brbr_chair_mutex = true; // occupied by barber to sleep //locked
        cout << "Shop Opened" << endl;
    }

    void customer_in()
    {
        if (sleep == true)
        {
            sleep = false;     // barber woke up
            brbr_chair_mutex = true; // occupied by customer //locked
            cout << "Customer *IN*.\nBarber woke up, customer occupied his seat." << endl;
            // customer_out();
            return;
        }
        else
        {
            if (avl_chairs == 0)
            {
                cout << "No Space, Customer Leaves" << endl;
            }
            else if (avl_chairs > 0)
            {
                avl_chairs--;
                cout << "Customer Occupied Waiting seat, Avaliable seats: " << avl_chairs << endl;
            }
        }
    }
    void customer_out()
    {
        if (avl_chairs == 3)
        {

            sleep = true;      // barber sleeps
            brbr_chair_mutex = true; // occupied by barber
            cout << "All Customers *OUT*.\nBarber sleeps" << endl;
        }
        else
        {
            avl_chairs++;
            brbr_chair_mutex = true; // occupied by next customer // unlocked by previos customer and then locked occupied by the next customer
            cout << "Next Customer Occupied Barber seat, Avaliable seats: " << avl_chairs << endl;
        }
    }
};

int main()
{
    Shop s;
    s.customer_in();  // 1st customer occpies barber seat avl = 3;
    s.customer_in();  // 2st customer occpies wating seat avl = 2;
    s.customer_in();  // 3st customer occpies wating seat avl = 1;
    s.customer_in();  // 4st customer occpies wating seat avl = 0;
    s.customer_in();  // 5st customer leaves as avl = 0;
    s.customer_out(); // 1st customer leaves avl = 1;
    s.customer_in();  // 5st customer occpies wating seat avl = 0;
    s.customer_in();  // 6st customer leaves as avl = 0;
    s.customer_out(); // 2st customer leaves avl = 1;
    s.customer_out(); // 3st customer leaves avl = 2;
    s.customer_out(); // 4st customer leaves avl = 3.;
    s.customer_out(); // 5st customer leaves avl = 4(including barber seat);

    return 0;
}