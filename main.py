#include <iostream>
using namespace std;

struct Node
{
    int data;
    struct Node *next;
};

class LL
{
    Node *head;
    Node *curr;
    int nodes;
    public:
     LL()
     {
        head=curr=NULL;
        nodes=0;
     }
     void insertnode(int d)
     {
        Node *temp= new Node();
        temp->data=d;
        temp->next=NULL;

         if(head==NULL)
         {
             head=temp;
             curr=head;
             cout<<"inserted "<<d<<" as head"<<endl;
         }
         else
         {
             curr->next=temp;
             curr=curr->next;
             cout<<"inserted "<<d<<" node"<<endl;
         }
     }

     void display()
     {
         struct Node *temp= new Node();
         temp=head;
         cout<<endl;
         cout<<"ll is: "<<endl;
         while(temp!=NULL)
         {
             cout<<temp->data<<" ";
             temp=temp->next;
             nodes++;
         }
     }

     void insert_middle(int what, int where)
     {
         Node *ptr= new Node();
         ptr=head;
         cout<<"finding";
         int i=0;
         while(ptr->data!=where)
         {
             i++;
             ptr=ptr->next;
             if(i==nodes)
             {
                 break;
             }
         }
         cout<<"found"<<endl;
         struct Node *temp= new Node();
         temp->data=what;
         temp->next=ptr->next;
         ptr->next=temp;
     }

     void delete_node(int del)
     {
         Node *ptr= new Node();
         ptr=head;
         if(ptr->data == del)
         {
             head=ptr->next;
             ptr->next=NULL;
         }
         else
        {
            while(ptr->next->data != del)
             {
                 ptr=ptr->next;
             }
             Node *temp= new Node();
             temp=ptr->next;
             ptr->next=ptr->next->next;
             delete(temp);
         }
     }

     void rev()
     {
         Node *prev= new Node();
         Node *next= new Node();
         prev=next=NULL;
         curr=head;
         while(curr!=NULL)
         {
             next=curr->next;
             curr->next=prev;
             prev=curr;
             curr=next;
         }
         head=prev;
     }

     /*void rev_k(int k)
     {
         int s=0;
         curr=head;
         Node *prev= new Node();
         Node *next= new Node();
         while(curr!= NULL && s<k)
         {
             prev=next=NULL;
             curr=head;
             next=curr->next;
             curr->next=prev;
             prev=curr;
             curr=next;
             s++;
         }

        if (head != NULL)
        {
                head->next =curr;
         }

        s= 0;
        while(s < k-1 && curr != NULL )
        {
        curr = curr->next;
        s++;
        }

        if(curr != NULL)
            rev_k(k);

     }*/
};

int main()
{
    cout<<"hi"<<endl;
    LL l;
    l.insertnode(6);
    l.insertnode(10);
    l.insertnode(7);
    l.insertnode(8);
    l.insertnode(2);
    l.insertnode(9);
    l.insertnode(3);
    l.display();
    l.insert_middle(4,10);
    l.display();
    l.delete_node(8);
    l.display();
    l.rev();
    l.display();
    l.rev();
    l.display();
    return 0;
}
