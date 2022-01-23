def deleteDuplicates(self, head):
    if head == None:
        return None
    #If the head is null, just turn None
    node = head
    while node.next != None:
      # Keep iterating as long as node.next is available
        if node.val == node.next.val:
                #This means when they're the same, then duplicate item will be gone.
            node.next = node.next.next
        else:
            #go to next node if they're not the same.
            node = node.next
    return head
    #finall return head node.
