class Mahasiswa {
    public String name;
    public int age;

    Mahasiswa() {
    }

    Mahasiswa(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void display() {
        System.out.println("Halo nama saya " + this.name + ", umur saya " + this.age + " tahun");
    }
}

public class Main {
    public static void main(String args[]) {
        // System.out.println("Hello teman2 kita lagi belajar oop di java");

        // instansiasi object
        Mahasiswa mhs = new Mahasiswa();
        mhs.name = "parjo";
        mhs.age = 300;
        mhs.display();
    }
}