rows = 5

start = 0

while start < rows:
        # Calculate spaces needed for centering
        spaces = " " * (rows - start - 1)
        
        # Calculate stars for the current row (odd number of stars for a symmetrical pyramid)
        stars = "*" * (2 * start + 1)
        
        # Print the row
        print(spaces + stars)
        
        # Move to the next row
        start += 1


