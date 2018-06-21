using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Xml.Serialization;

/// <remarks/>
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
[System.Xml.Serialization.XmlRootAttribute(Namespace = "http://www.example.org/typy", IsNullable = false, ElementName = "wypożyczalnia")]
public partial class CarRental
{

    private wypożyczalniaOpis opisField;

    private ObservableCollection<wypożyczalniaSamochód> samochodyField;

    private wypożyczalniaUsługi usługiField;

    /// <remarks/>
    public wypożyczalniaOpis opis
    {
        get
        {
            return this.opisField;
        }
        set
        {
            this.opisField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlArrayItemAttribute("samochód", IsNullable = false)]
    public ObservableCollection<wypożyczalniaSamochód> samochody
    {
        get
        {
            return this.samochodyField;
        }
        set
        {
            this.samochodyField = value;
        }
    }

    /// <remarks/>
    public wypożyczalniaUsługi usługi
    {
        get
        {
            return this.usługiField;
        }
        set
        {
            this.usługiField = value;
        }
    }
}

/// <remarks/>
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class wypożyczalniaOpis
{

    private string tematField;

    private ObservableCollection<wypożyczalniaOpisAutor> autorzyField;

    /// <remarks/>
    public string temat
    {
        get
        {
            return this.tematField;
        }
        set
        {
            this.tematField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlArrayItemAttribute("autor", IsNullable = false)]
    public ObservableCollection<wypożyczalniaOpisAutor> autorzy
    {
        get
        {
            return this.autorzyField;
        }
        set
        {
            this.autorzyField = value;
        }
    }
}

/// <remarks/>
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class wypożyczalniaOpisAutor
{

    private string imieField;

    private string nazwiskoField;

    private uint nr_indeksuField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string imie
    {
        get
        {
            return this.imieField;
        }
        set
        {
            this.imieField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string nazwisko
    {
        get
        {
            return this.nazwiskoField;
        }
        set
        {
            this.nazwiskoField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public uint nr_indeksu
    {
        get
        {
            return this.nr_indeksuField;
        }
        set
        {
            this.nr_indeksuField = value;
        }
    }
}

/// <remarks/>
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class wypożyczalniaSamochód
{
    
    private wypożyczalniaSamochódNazwa nazwaField;

    private wypożyczalniaSamochódPrzebieg przebiegField;

    private ushort rok_produkcjiField;

    private string kolorField;

    private string czy_wypożyczoneField;

    private wypożyczalniaSamochódMiasto miastoField;

    private wypożyczalniaSamochódCena_wypożyczenia_za_1_dzien cena_wypożyczenia_za_1_dzienField;

    private string idField;

    /// <remarks/>
    public wypożyczalniaSamochódNazwa nazwa
    {
        get
        {
            return this.nazwaField;
        }
        set
        {
            this.nazwaField = value;
        }
    }

    /// <remarks/>
    public wypożyczalniaSamochódPrzebieg przebieg
    {
        get
        {
            return this.przebiegField;
        }
        set
        {
            this.przebiegField = value;
        }
    }

    /// <remarks/>
    public ushort rok_produkcji
    {
        get
        {
            return this.rok_produkcjiField;
        }
        set
        {
            this.rok_produkcjiField = value;
        }
    }

    /// <remarks/>
    public string kolor
    {
        get
        {
            return this.kolorField;
        }
        set
        {
            this.kolorField = value;
        }
    }

    /// <remarks/>
    public string czy_wypożyczone
    {
        get
        {
            return this.czy_wypożyczoneField;
        }
        set
        {
            this.czy_wypożyczoneField = value;
        }
    }

    /// <remarks/>
    public wypożyczalniaSamochódMiasto miasto
    {
        get
        {
            return this.miastoField;
        }
        set
        {
            this.miastoField = value;
        }
    }

    /// <remarks/>
    public wypożyczalniaSamochódCena_wypożyczenia_za_1_dzien cena_wypożyczenia_za_1_dzien
    {
        get
        {
            return this.cena_wypożyczenia_za_1_dzienField;
        }
        set
        {
            this.cena_wypożyczenia_za_1_dzienField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string id
    {
        get
        {
            return this.idField;
        }
        set
        {
            this.idField = value;
        }
    }
}

/// <remarks/>
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class wypożyczalniaSamochódNazwa
{

    private string modelField;

    private string markaField;

    private string generacjaField;

    /// <remarks/>
    public string model
    {
        get
        {
            return this.modelField;
        }
        set
        {
            this.modelField = value;
        }
    }

    /// <remarks/>
    public string marka
    {
        get
        {
            return this.markaField;
        }
        set
        {
            this.markaField = value;
        }
    }

    /// <remarks/>
    public string generacja
    {
        get
        {
            return this.generacjaField;
        }
        set
        {
            this.generacjaField = value;
        }
    }
}

/// <remarks/>
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class wypożyczalniaSamochódPrzebieg
{

    private string jednostkaField;

    private uint valueField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string jednostka
    {
        get
        {
            return this.jednostkaField;
        }
        set
        {
            this.jednostkaField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlTextAttribute()]
    public uint Value
    {
        get
        {
            return this.valueField;
        }
        set
        {
            this.valueField = value;
        }
    }
}

/// <remarks/>
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class wypożyczalniaSamochódMiasto
{

    private string miastoField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string miasto
    {
        get
        {
            return this.miastoField;
        }
        set
        {
            this.miastoField = value;
        }
    }
}

/// <remarks/>
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class wypożyczalniaSamochódCena_wypożyczenia_za_1_dzien
{

    private string walutaField;

    private decimal valueField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string waluta
    {
        get
        {
            return this.walutaField;
        }
        set
        {
            this.walutaField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlTextAttribute()]
    public decimal Value
    {
        get
        {
            return this.valueField;
        }
        set
        {
            this.valueField = value;
        }
    }
}

/// <remarks/>
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class wypożyczalniaUsługi
{

    private ObservableCollection<wypożyczalniaUsługiPracownik> pracownicyField;

    private ObservableCollection<wypożyczalniaUsługiWypożyczenie> wypożyczeniaField;

    /// <remarks/>
    [System.Xml.Serialization.XmlArrayItemAttribute("pracownik", IsNullable = false)]
    public ObservableCollection<wypożyczalniaUsługiPracownik> pracownicy
    {
        get
        {
            return this.pracownicyField;
        }
        set
        {
            this.pracownicyField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlArrayItemAttribute("wypożyczenie", IsNullable = false)]
    public ObservableCollection<wypożyczalniaUsługiWypożyczenie> wypożyczenia
    {
        get
        {
            return this.wypożyczeniaField;
        }
        set
        {
            this.wypożyczeniaField = value;
        }
    }
}

/// <remarks/>
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class wypożyczalniaUsługiPracownik
{

    private string imieField;

    private string nazwiskoField;

    private string idField;

    /// <remarks/>
    public string imie
    {
        get
        {
            return this.imieField;
        }
        set
        {
            this.imieField = value;
        }
    }

    /// <remarks/>
    public string nazwisko
    {
        get
        {
            return this.nazwiskoField;
        }
        set
        {
            this.nazwiskoField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string id
    {
        get
        {
            return this.idField;
        }
        set
        {
            this.idField = value;
        }
    }
}

/// <remarks/>
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class wypożyczalniaUsługiWypożyczenie
{

    private string data_wypożyczeniaField;

    private string data_zwrotuField;

    private wypożyczalniaUsługiWypożyczenieWypożyczający wypożyczającyField;

    private string id_pracownikaField;

    private string id_samochoduField;

    /// <remarks/>
    public string data_wypożyczenia
    {
        get
        {
            return this.data_wypożyczeniaField;
        }
        set
        {
            this.data_wypożyczeniaField = value;
        }
    }

    /// <remarks/>
    public string data_zwrotu
    {
        get
        {
            return this.data_zwrotuField;
        }
        set
        {
            this.data_zwrotuField = value;
        }
    }

    /// <remarks/>
    public wypożyczalniaUsługiWypożyczenieWypożyczający wypożyczający
    {
        get
        {
            return this.wypożyczającyField;
        }
        set
        {
            this.wypożyczającyField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string id_pracownika
    {
        get
        {
            return this.id_pracownikaField;
        }
        set
        {
            this.id_pracownikaField = value;
        }
    }
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string id_samochodu
    {
        get
        {
            return this.id_samochoduField;
        }
        set
        {
            this.id_samochoduField = value;
        }
    }
}

/// <remarks/>
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class wypożyczalniaUsługiWypożyczenieWypożyczający
{

    private string imieField;

    private string nazwiskoField;

    private ulong peselField;

    private string nr_telefonuField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string imie
    {
        get
        {
            return this.imieField;
        }
        set
        {
            this.imieField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string nazwisko
    {
        get
        {
            return this.nazwiskoField;
        }
        set
        {
            this.nazwiskoField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public ulong pesel
    {
        get
        {
            return this.peselField;
        }
        set
        {
            this.peselField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string nr_telefonu
    {
        get
        {
            return this.nr_telefonuField;
        }
        set
        {
            this.nr_telefonuField = value;
        }
    }
}
