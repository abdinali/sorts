package insertionsort;

import java.util.ArrayList;
import java.util.List;

public class InsertionSort {
    public static void main(String[] args) {
        List<Integer> inputValues = new ArrayList<>();
        inputValues.add(1);
        inputValues.add(7);
        inputValues.add(3);
        inputValues.add(2);
        inputValues.add(6);

        System.out.println("Before: " + inputValues.toString());
        // Insertion Sort
        for (int j = 1; j < inputValues.size(); j++) {
            int temp = inputValues.get(j);
            int i = j - 1;
            while (i >= 0 && inputValues.get(i) > temp) {
                inputValues.set(i + 1, inputValues.get(i));
                i = i - 1;
            }
            inputValues.set(i + 1, temp);
        }
        System.out.println("After: " + inputValues.toString());
    }
}
