import streamlit as st

def synthetic_division(coefficients, divisor):
    """
    Perform synthetic division on a polynomial divided by (x - divisor).

    Parameters:
        coefficients (list): Polynomial coefficients [a_n, a_(n-1), ..., a_0]
        divisor (float): The constant 'c' in (x - c)

    Returns:
        tuple: (quotient coefficients, remainder)
    """
    n = len(coefficients)
    result = [coefficients[0]]  # Bring down the first coefficient

    # Perform synthetic division algorithm
    for i in range(1, n):
        value = coefficients[i] + result[-1] * divisor
        result.append(value)

    quotient = result[:-1]
    remainder = result[-1]
    return quotient, remainder

st.set_page_config(page_title="Synthetic Division Calculator", page_icon="563361769_715548754133610_3020252312267426014_n.png", layout="centered")

st.title("Synthetic Division Calculator")
st.write("Divide a polynomial by a binomial")


coeff_str = st.text_input(
    "Enter the coefficients of the polynomial (comma-separated):",
    placeholder="e.g., 2, 3, -5, 6"
)
divisor = st.number_input(
    "Enter the divisor (the 'c' in x - c):",
    value=2.0,
    step=0.1,
    format="%.2f"
)

if st.button("Calculate"):
    try:
        coefficients = [float(x.strip()) for x in coeff_str.split(",") if x.strip() != ""]
        if not coefficients:
            st.warning("Please enter at least one coefficient.")
        else:
            quotient, remainder = synthetic_division(coefficients, divisor)

            st.success(" Division complete")
            st.write(f"**Quotient coefficients:** {quotient}")
            st.write(f"**Remainder:** {remainder}")
            degree = len(quotient) - 1
            terms = []
            for i, coeff in enumerate(quotient):
                power = degree - i
                coeff_str = f"{coeff:.2f}".rstrip("0").rstrip(".")
                if power > 1:
                    terms.append(f"{coeff_str}x^{power}")
                elif power == 1:
                    terms.append(f"{coeff_str}x")
                else:
                    terms.append(f"{coeff_str}")
            quotient_poly = " + ".join(terms).replace("+ -", "- ")
            st.write("**Quotient Polynomial:**")
            st.latex(quotient_poly)
            if remainder != 0:
                st.write("**Result in full form:**")
                st.latex(f"({quotient_poly}) + \\frac{{{remainder:.2f}}}{{x - ({divisor})}}")
    except Exception as e:
        st.error(f"Error: {e}")
st.markdown("---")
st.caption("Made by Kurt Cabase using Streamlit and Python 3.14")
