import ThetaPrimeTrace

open Formalism.BasicNotions GlobalTheory.ChainOnto GlobalTheory.ChainOnto.ParClosed
open NumberField IsDedekindDomain ThetaTransfer
attribute [local instance] Formalism.BasicNotions.Host.cmStar

noncomputable section
namespace EisensteinPrimeRace

def chiFour (n : ℕ) : ℂ :=
  if n % 4 = 1 then 1 else if n % 4 = 3 then -1 else 0

def window (b t : ℝ) : ℝ :=
  if 1 < t ∧ t ≤ b then b * (1 - 1 / t)
  else if b < t ∧ t < b^2 then b^2 / t - 1 else 0

variable {D : D7}

def normWeight (b y : ℝ) (w : HeightOneSpectrum (𝓞 D.host.E)) : ℂ :=
  let q : ℝ := Ideal.absNorm w.asIdeal
  (Real.log q * window b (q / y) : ℝ)

/-- If an admissible row realizes the character of the norm modulo four on
the places in the window, the trace difference equals the signed race. -/
theorem trace_eq_norm_race (c : Com D) (base : GlobalTheory.LFun.Fam D.host.E)
    (k : ℕ) (places : Finset (HeightOneSpectrum (𝓞 D.host.E))) (b y : ℝ)
    (hchar : ∀ w ∈ places,
      ((vf (c.chS (k+1)) w : ℂˣ) : ℂ) = chiFour (Ideal.absNorm w.asIdeal)) :
    (∑ w ∈ places, normWeight b y w * ((firstTrace (chainPar c base (k+1) w) -
       ((vf (c.chS (k+1) * (c.chT (k+1))⁻¹) w : ℂˣ) : ℂ) *
          firstTrace (chainPar c base k w)) /
       firstTrace (GlobalTheory.LFun.seg w 1 D.R.t))) =
    (∑ w ∈ places.filter (fun w => Ideal.absNorm w.asIdeal % 4 = 1), normWeight b y w) -
    (∑ w ∈ places.filter (fun w => Ideal.absNorm w.asIdeal % 4 = 3), normWeight b y w) := by
  classical
  rw [theta_prime_trace_extract, Finset.sum_filter, Finset.sum_filter,
      ← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro w hw
  rw [hchar w hw]
  by_cases h : Ideal.absNorm w.asIdeal % 4 = 1
  · have h' : Ideal.absNorm w.asIdeal % 4 ≠ 3 := by omega
    simp [chiFour, h, h']
  · by_cases h' : Ideal.absNorm w.asIdeal % 4 = 3 <;> simp [chiFour, h, h']

#print axioms EisensteinPrimeRace.trace_eq_norm_race
end EisensteinPrimeRace
