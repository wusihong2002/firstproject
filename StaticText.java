public class StaticText {
    public static void main(String[] args){
        var staff = new Employee[3];
        staff[0]=new Employee("tom",40000);
        staff[1]=new Employee("dike",20000);
        staff[2]=new Employee("harry",45000);
        for (Employee e :staff){
            e.setId();
            e.raiseSalary(5);
            System.out.println("name="+e.getName()+",id="+e.getId()+",salary="+e.getSalary());
        }
        int n= Employee.getNextId();
        System.out.println("next available id="+n);

    }


}
class Employee {
    private static int nextId = 1;
    private String name;
    private double salary;
    private  int id;
    public Employee(String n, double s){
        name=n;
        salary=s;
        id=0;
    }
    public String getName(){
        return name;
    }
    public double getSalary(){
        return salary;
    }
    public int getId(){
        return id;
    }
    public  void setId(){
        id=nextId;
        nextId++;
    }
    public static int getNextId(){
        return nextId;
    }
    public static void main(String[] args){
        var e=new  Employee("张三",70000);
        System.out.println(e.getName()+" "+e.getSalary());
    }
    public void raiseSalary(double byPercent){
        double raise=salary*byPercent/100;
        salary+=raise;
    }
}