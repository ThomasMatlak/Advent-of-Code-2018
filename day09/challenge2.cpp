#include <algorithm>
#include <iostream>
#include <vector>

#define NUM_PLAYERS 403
#define LAST_MARBLE_NUM 7192000

struct Marble
{
    int value;
    Marble* next;
    Marble* prev;
};

class LinkedList
{
    private:
    Marble* currentMarble;
    int size;

    public:
    LinkedList()
    {
        Marble* marble = new Marble;

        marble->value = 0;
        marble->next = marble;
        marble->prev = marble;

        size = 1;
        currentMarble = marble;
    }

    ~LinkedList()
    {
        while ( size > 0 )
        {
            currentMarble->prev->next = currentMarble->next;
            currentMarble->next->prev = currentMarble->prev;
            Marble* next = currentMarble->next;
            delete currentMarble;
            currentMarble = next;
            --size;
        }
    }

    void addMarble( int value )
    {
        Marble* oneClockwise = currentMarble->next;
        Marble* twoClockwise = oneClockwise->next;

        Marble* marble = new Marble;
        marble->value = value;
        marble->next = twoClockwise;
        marble->prev = oneClockwise;

        oneClockwise->next = marble;
        twoClockwise->prev = marble;

        currentMarble = marble;
        ++size;
    }

    int removeMarble()
    {
        Marble* marbleToRemove = currentMarble->prev->prev->prev->prev->prev->prev->prev;
        currentMarble = marbleToRemove->next;
        int value = marbleToRemove->value;
        
        marbleToRemove->prev->next = marbleToRemove->next;
        marbleToRemove->next->prev = marbleToRemove->prev;

        --size;
        return value;
    }
};

int main(int argc, char const *argv[])
{
    std::vector<long> players( NUM_PLAYERS, 0 );

    LinkedList circle = LinkedList();

    int playerNum = 0;

    for ( int marble_number = 1; marble_number <= LAST_MARBLE_NUM; ++marble_number )
    {
        if ( marble_number % 23 == 0 )
        {
            players[playerNum] += marble_number;
            players[playerNum] += circle.removeMarble();
        }
        else
        {
            circle.addMarble( marble_number );
        }

        ++playerNum;
        playerNum %= NUM_PLAYERS;
    }

    std::cout << *std::max_element( players.begin(), players.end() ) << std::endl;

    return 0;
}
