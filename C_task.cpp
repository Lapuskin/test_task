/*1) Реализовать с использованием библиотеки MFC без использования STL*/
#include <iostream>
#include <memory>
#include <vector>
#include <string>

typedef CMap<CString, LPCTSTR, CString, CString&> CMapSSSS;
typedef enum {
	CHANGE_NOCHANGES, CHANGE_TOLOWER, CHANGE_TOUPPER,
	CHANGE_CHARLOWER, CHANGE_CHARUPPER
} LETTER_CHANGE;


/************************************/
/*Написать реализацию данной функции*/
CMapSSSS* ExplodeStringToMapSSSS(const CString& sString,
	const CString& sSeparatorExt, const CString& sSeparatorInt,
	const int& nHashSize, CMapSSSS* pDstMap, LETTER_CHANGE nChange)
{	

	int indexExt, indexInt, prevIndexExt = 0; 
	while ((indexExt = sString.Find(sSeparatorExt)) != -1)
	{
		CString sTemp =  sString.Mid(prevIndexExt, indexExt - prevIndexExt);
		indexInt = sTemp.Find(sSeparatorInt);
		CString sKey = sTemp.Left(indexInt);
		CString sValue = sTemp.Right(sTemp.GetLenght() - indexInt - 1);

		switch (nChange)
			{
			case CHANGE_TOLOWER:
				sValue.MakeLower();
				break;
			case CHANGE_TOUPPER:
				sValue.MakeUpper();
				break;
			case CHANGE_CHARLOWER:
				sValue.SetAt(0, tolower(sValue.GetAt(0)));
				break;
			case CHANGE_CHARUPPER:
				sValue.SetAt(0, toupper(sValue.GetAt(0)));
				break;
			default:
				break;
			}

		if (pDstMap)
				pDstMap->SetAt(sKey, sValue);
		prevIndexExt = indexExt + 1;
	}
	return pDstMap;
};	


/*
sString -> Сама строка вида abc,zgd;vng,jsdasd;...
sSeparatorExt -> Разделитель между элементами карты (в примере выше это ";"")
sSeparatorInt -> Разделитель между ключем/значением (в примере выше это ",")
nHashSize -> Размер хеша для карты
pDstMap -> Указатель на исходную карту, в которую требуется (если он есть) записать результат и вернуть
nChange -> Тип операции над ключем перед помещением его в карту
		TOLOWER -> перевести всю строку в нижний регистр
		TOUPPER -> перевести всю строку в верхний регистр
		CHARLOWER -> первый символ строки сделать в нижнем регистре
		CHARUPPER -> первый символ строки сделать в верхнем регистре
*/

/*2) Реализовать иерархию классов Widget, где Widget - это базовый класс,
 	а TabWidget и CalendarWidget - это конкретные реализации базового класса.
  	Каждый виджет может хранить сколько угодно дочерних виджетов. 
  	Каждый виджет хранит указатель на родительский виджет, родительских виджетов не может быть несколько, только один.
   	Так же необходимо реализовать метод, позволяющий идентифицировать тип конкретного виджета.
	В реализации использовать умные указатели.*/

class Widget : public std::enable_shared_from_this<Widget> {
protected:
    std::shared_ptr<Widget> parentWidget;
    std::vector<std::shared_ptr<Widget>> internalWidgets;

public:
    void setParent(std::shared_ptr<Widget> parent) {
        parentWidget = parent;
    }

    std::shared_ptr<Widget> getParent() {
        return parentWidget;
    }

    void addWidget(std::shared_ptr<Widget> widget) {
        widget->setParent(shared_from_this());
        internalWidgets.push_back(widget);
    }

    virtual std::string identify() const = 0;
};

class TabWidget : public Widget {
public:
    std::string identify() const override {
        return "TabWidget";
    }
};

class CalendarWidget : public Widget {
public:
    std::string identify() const override {
        return "CalendarWidget";
    }
};
