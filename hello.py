import streamlit as st
st.title("hello world!")
st.write("練習")
st.text_input("   ")
st.radio(label: 練習 str, options: Union[Sequence[Any], pandas.core.frame.DataFrame, pandas.core.series.Series, pandas.core.indexes.base.Index, numpy.ndarray], index: int = 0, format_func: Callable[[Any], Any] = <class 'str'>, key: Union[str, int, NoneType] = None, help: Union[str, NoneType] = None, on_change: Union[Callable[..., NoneType], NoneType] = None, args: Union[Tuple[Any, ...], NoneType] = None, kwargs: Union[Dict[str, Any], NoneType] = None, *, disabled: bool = False) -> Any