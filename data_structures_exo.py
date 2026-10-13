'''
# playlist manager
'''
'''
Exercise 1 – Playlist manager

Display the first and the last song using indexes. Expected: Intro Echoes
Add "Outro" at the end, then "Prelude" at the beginning.
Remove "Blue Moon" by its value.
Remove the song at index 2 with pop() and display the removed song. Expected: Sunrise
Display the number of songs and check whether "Echoes" is in the playlist. Expected: 4 True
Using slicing only, display the first 3 songs, then the whole playlist reversed. Expected: ['Prelude', 'Intro', 'Echoes'] and ['Outro', 'Echoes', 'Intro', 'Prelude']
Display the playlist sorted alphabetically without modifying it, then display the playlist again to check.
Question: what is the difference between playlist.sort() and sorted(playlist)? What does print(playlist.sort()) display, and why?
'''

playlist = ["Intro", "Sunrise", "Blue Moon", "Echoes"]

print(playlist[0], playlist[-1])
playlist.remove("Blue Moon")
print(playlist.pop(1))

print(playlist)