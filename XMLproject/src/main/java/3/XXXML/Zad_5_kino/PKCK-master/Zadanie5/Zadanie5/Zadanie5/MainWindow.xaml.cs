using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using Zadanie5.Pages;
using Zadanie5.ViewModel;

namespace Zadanie5
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private MainViewModel _vm;
        public MainWindow()
        {
            InitializeComponent();
            carFrame.Navigate(new DisplayCars());
            employeesFrame.Navigate(new DisplayEmployees());
            rentalsFrame.Navigate(new DisplayRentals());

            Loaded += MainWindow_Loaded;
        }

        private void MainWindow_Loaded(object sender, RoutedEventArgs e)
        {
            _vm = DataContext as MainViewModel;
        }

        //For some reason binding it's not working

        private void DeleteCar(object sender, RoutedEventArgs e)
        {
            _vm.DeleteCarCommand.Execute(null);
        }

        private void DeleteRental(object sender, RoutedEventArgs e)
        {
            _vm.DeleteRentalCommand.Execute(null);
        }

        private void DeleteEmployee(object sender, RoutedEventArgs e)
        {
            _vm.DeleteEmployeeCommand.Execute(null);
        }

        private void AddCar(object sender, RoutedEventArgs e)
        {
            carFrame.Navigate(new AddCar());
        }

        private void AddRental(object sender, RoutedEventArgs e)
        {
            rentalsFrame.Navigate(new AddRental());
        }

        private void AddEmployee(object sender, RoutedEventArgs e)
        {
            employeesFrame.Navigate(new AddEmployee());
        }

        private void ConfirmCar(object sender, RoutedEventArgs e)
        {
            _vm.AddCarCommand.Execute(null);
            carFrame.GoBack();
        }

        private void ConfirmRental(object sender, RoutedEventArgs e)
        {
            _vm.AddRentalCommand.Execute(null);
            rentalsFrame.GoBack();
        }

        private void ConfirmEmployee(object sender, RoutedEventArgs e)
        {
            _vm.AddEmployeeCommand.Execute(null);
            employeesFrame.GoBack();
        }
    }
}
