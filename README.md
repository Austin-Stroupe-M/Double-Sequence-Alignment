# Double-Sequence-Alignment
## Introduction
This python script takes two RNA sequences and three score values. From those sequences and values it calculates the optimal alignment of the two sequences based on the provided scores.

## Features
- Prints score array
- Prints backtracking array
- Prints the sequences with proper alignment including gaps
- Prints the final optimal score
- Allows for multiple runs without termination

## Requirements
- [Python](https://www.python.org/downloads/) v3.0 or better

## Installation
1. Download the current [Seq_Align](https://github.com/Austin-Stroupe-M/Double-Sequence-Alignment) python file from the github repository. It should be in the form Seq_AlignVX_Y.py where **X** and **Y** will be numbers
2. Move the file to your intended directory

## Use
1. **Double Click** the file to run the script. 
- *This will open a **console**.*
2. Once the console is open it will prompt you to enter the first RNA sequence. This sequence should only contain **letters**. Type your RNA sequence in the console and hit **ENTER**.
-  `Enter Sequence 1: CGAUCAC`
3. The console will prompt you for a second sequence. Repeat **Step 2** with a new sequence. 
- `Enter Sequence 2: CAUCGAC`
4. The console will now prompt you to enter a match score. This value should be a **positive integer**. Type your number value and hit **ENTER**.
- `Enter match score: 6`
5. Now you will input your mismatch score. This value should be a **negative integer or zero**. 
- `Enter mismatch score: -4`
6. Finally, you will input your gap penalty. This value should be a **negative integer or zero**. 
- `Enter gap penalty: -3`
7. The script will now generate your score matrix, your backtracking matrix, the alignment of the two sequences, and the optimal score. All of this will be printed to the console.
- A full run of the program should look like the following:

![A full run should look like this.](Sample.PNG)

- You can now choose if you want to run the script again.
- *Type the letter **Y** to run again or type **N** to stop and close the script.*
- `Run again? (Y/N): N`

## FAQs
- Q: What happens if I input a number in the sequence?
- A: Nothing will immediately happen or break but your results will be nonsense.
- Q: What happens if I input a letter for the match/mismatch/gap scores?
- A: The script will immediately crash. This will be fixed in a future update.
- Q: Can I save my results?
- A: In the previous version all results would be saved in a file automatically but this was changed to printing to the console for ease of use. In a future update you will be able to choose to save your results or not.

## Troubleshooting/Support
If you encounter problems make sure you have python installed and that the version is 3.0 or above. If that does not fix your issue feel free to contact me at [austin.stroupe.m@gmail.com](austin.stroupe.m@gmail.com).

## Contributions
The source code is available and you are welcome to submit push requests.

## Licensing
[MIT](https://choosealicense.com/licenses/mit/)
